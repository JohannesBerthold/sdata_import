#!/usr/bin/env python
import pandas as pd
import numpy as np
import sys
import os
import matplotlib
import matplotlib.pyplot as plt

class Diagramm():
  def __init__(self, file_name):
    self._df = None
    self._X = None
    self._Y = None
    self._file = file_name
  
  def read(self):
    fig, ax = plt.subplots()
    self._df = pd.read_csv(self._file, header = None, skiprows=9, sep=",", names = ["s", "F"])
    nxy = len(self._df.columns)      
    self._X = self._df["s"]
    self._Y = self._df["F"]
    ax.plot([self._X],[self._Y])
    plt.show
    
if __name__ == '__main__':
    test_object = Diagramm("aluTL114-UT22-h11-n1.csv")
    test_object.read()
    