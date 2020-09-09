# -*- coding: utf-8 -*-

from __future__ import print_function

import pandas as pd
import os

DB_dir = '../datasets'
DB_csv = 'data.csv'

class Database(object):

  def __init__(self):
    self.data = pd.read_csv(os.path.join(DB_dir, DB_csv))
    self.classes = set(self.data["cls"])

  def __len__(self):
    return len(self.data)

  def get_class(self):
    return self.classes

  def get_data(self):
    return self.data


if __name__ == "__main__":
  db = Database()
  data = db.get_data()
  classes = db.get_class()

  print("DB length:", len(db))
  print(classes)
