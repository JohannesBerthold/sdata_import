# -*-coding: utf-8-*-

from __future__ import division
__version__ = '0.1.0'
__revision__ = None
__version_info__ = tuple([int(num) for num in __version__.split('.')])
__copyright__ = '(c) Scale GmbH'


import os
import sys
import time
import pandas as pd
import random
import numpy as np
import sdata
print(sdata.__version__)
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox, QWidget
# from PyQt5.QtGui import QPalette
from numpy import arange, sin, pi
import matplotlib
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas


class Measurement(object):
    def __init__(self, file_path):
        self._df = None
        self._dfall = None
        self._s = None
        self._f = None
        self._read_excel_df(file_path)

    def _read_df(self, file_path):
    
        if os.path.exists(file_path):
            self._df = pd.read_csv(file_path, header=None, skiprows=9, sep=",", names=["s", "F"])    
            self._s = self._df["s"]
            self._f = self._df["F"]
        else:
            raise ValueError("File unknown: {0}".format(file_path))

    def _read_excel_df(self, file_path):
    
        if os.path.exists(file_path):
            self._df = pd.read_excel(file_path, sheetname= "Daten", header= None, skiprows=3, parse_cols= None)
            anzversuche = 0
            sel_cols = []
            df = self._df.dropna(axis=1, how='all')

            print(df.tail())
            for i in range (0, self._df.shape[1]):
                if type(self._df[i][0]) in [float, np.float64, np.float32, np.float16]:
                    sel_cols.append(i)
            dfall = self._df.dropna(axis=1, how='all')

            # df = df[[1,2]].rename(columns= {1:"F", 2:"s"})
            testseries = sdata.testseries.TestSeries(name="testseries A1")
            testseries.metadata.set_attr(name="a", value=1.2, unit="MPa", description="a float", dtype="float")
            testprogramm = sdata.TestProgram()
            testprogramm.metadata.set_attr(name="ProgrammA", value=1.2)

            for idxs in [[1,2], [6,7], [11,12], [16,17], [21,22]]:
                print(idxs)
                df = dfall[idxs]
                df.columns = ["s", "F"]
                singletest = sdata.test.Test(name="test 001")
                singletest.metadata.set_attr(name="failure_type", value="SH", unit="-", description="shear failure", dtype="str")
                table = sdata.Table()
                table.data = df
                table.metadata.set_attr(name="result_type", value="force_displacement", unit="-", description="?", dtype="str")

                singletest.add_result(table)
                testseries.add_test(singletest)
                testprogramm.add_series(testseries)

                print(df.head())
                print(singletest)

            print(testseries)
            print(testseries.metadata)
            print (testprogramm)
            print (testprogramm.metadata)
            testprogramm.exportpath = "/tmp/"
            print (testprogramm)

            #print self._df
            #self._df = pd.read_excel(file_path, sheetname= "Daten", header= None, skiprows=3, names=["s", "F"], parse_cols= [1, 2])

       # print self._df
        else:
            raise ValueError("File unknown: {0}".format(file_path))

        return testseries

    def get_data(self):
        return self._df

if __name__ == '__main__':
    f = []
    root_path = "/method/fosta"
    for (dirpath, dirnames, filenames) in os.walk(root_path):
        for index, file_i in enumerate(filenames):
            if file_i.endswith("xlsx"):
                f.append(os.path.join(dirpath, file_i))
    print(f[0])
    measurement = Measurement(f[0])

    # app = QApplication(sys.argv)
    #
    # aw = PlotWidget(measurement)
    # aw.setWindowTitle("PyQt5 Matplot Example")
    # aw.show()
    #
    # app.exec_()