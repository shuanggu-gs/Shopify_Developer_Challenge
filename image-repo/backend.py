from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import json
import numpy as np
import pandas as pd
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from CBIR.evaluate import infer
from CBIR.DB import Database

from CBIR.color import Color
from CBIR.daisy import Daisy
from CBIR.edge import Edge

import cgi
import io
from PIL import Image

import uuid


DATA_PATH = "../datasets/data.csv"

def get_similar(image):
    db = Database()
    method = Color()
    samples = method.make_samples(db)
    # make sure image is ndarray
    query = {'img': str(uuid.uuid1()), 'cls': 'TBD', 'hist': method.histogram(image)}
    _, result = infer(query, samples=samples)
    return [r['url'] for r in result]

def get_urls(tag = None, image = None):
    images_df = pd.read_csv(DATA_PATH)
    images_df = images_df.reindex(np.random.permutation(images_df.index))
    if tag:
        return {'url': list(images_df[images_df.cls == tag].url)}
    if image is not None:
        ans = get_similar(image)
        if len(ans):
            return {'url': ans}

    return {'url': list(images_df.url)}

class MyWebServer(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        im = None
        img_IO = form['image'].file.read()
        if img_IO:
            im = Image.open(io.BytesIO(img_IO))
            im = np.array(im)
        tag = form['tag'].value
        data = get_urls(tag, im)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        self.wfile.write(json.dumps(data).encode('utf-8'))
        return

    def do_GET(self):
        # 200: all is well, prepared to receive information
        self.send_response(200)
        # the format that we are gonna to receive info

        if 'frontend.css' in self.path:
            self.send_header('Content-type', 'text/css; charset=utf-8')
            self.end_headers()
            f = open("frontend.css", encoding='utf-8')
            html = f.read()
            f.close()
            self.wfile.write(html.encode('utf-8'))
        if 'frontend.js' in self.path:
            self.send_header('Content-type', 'text/javascript; charset=utf-8')
            self.end_headers()
            f = open("frontend.js", encoding='utf-8')
            html = f.read()
            f.close()
            self.wfile.write(html.encode('utf-8'))
        if self.path == '/':
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            f = open("frontend.html", encoding='utf-8')
            html = f.read()
            f.close()
            self.wfile.write(html.encode('utf-8'))

        return


if __name__ == '__main__':
    http_port = 9998
    server = HTTPServer(('localhost', http_port),  MyWebServer)
    server.serve_forever()
