import pandas as pd
import numpy as np
import os
from io import BytesIO
import requests
from PIL import Image
import uuid

PATH = "../datasets"
data = []

def create_db():
    FILENAMES = os.listdir(PATH)
    for filename in FILENAMES:
        filepath = os.path.join(PATH, filename)
        if not filepath.endswith(".txt"):
            continue
        label = filename[:-4]
        if not os.path.exists(os.path.join(PATH, label)):
            os.mkdir(os.path.join(PATH, label))
        else:
            continue
        with open(filepath) as f:
            image_urls = f.readlines()
            count = 0
            for url in image_urls:
                if count == 100:
                    break
                try:
                    response = requests.get(url.strip(), timeout=1)
                    if response.status_code == 200 and len(response.content) > 10000:
                        try:
                            Image.open(BytesIO(response.content))
                            image_name = str(uuid.uuid1())
                            with open(os.path.join(PATH, label, image_name+".jpg"), 'wb') as f:
                                f.write(response.content)
                                count += 1
                                data.append([image_name, url.strip(), label])
                        except:
                            continue
    #
                except:
                    continue
        print(label, " is done!")

    image_df = pd.DataFrame(data, columns=['img', 'url', 'cls'])
    image_df.to_csv('./data.csv')

create_db()