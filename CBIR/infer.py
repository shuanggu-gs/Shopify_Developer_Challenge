# -*- coding: utf-8 -*-

from __future__ import print_function

from CBIR.evaluate import infer
from CBIR.DB import Database

from CBIR.color import Color
from CBIR.daisy import Daisy
from CBIR.edge  import Edge
from CBIR.gabor import Gabor
from CBIR.HOG   import HOG
from CBIR.vggnet import VGGNetFeat
from CBIR.resnet import ResNetFeat

depth = 5
d_type = 'd1'
query_idx = 0

if __name__ == '__main__':
  db = Database()

  # retrieve by color
  method = Color()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)

  # retrieve by daisy
  method = Daisy()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)

  # retrieve by edge
  method = Edge()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)

  # retrieve by gabor
  method = Gabor()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)

  # retrieve by HOG
  method = HOG()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)

  # retrieve by VGG
  method = VGGNetFeat()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)

  # retrieve by resnet
  method = ResNetFeat()
  samples = method.make_samples(db)
  query = samples[query_idx]
  _, result = infer(query, samples=samples, depth=depth, d_type=d_type)
  print(result)
