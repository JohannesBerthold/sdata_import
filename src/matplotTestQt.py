#!/usr/bin/env python
# -*-coding: utf-8-*-

from __future__ import division
__version__ = '0.1.0'
__revision__ = None
__version_info__ = tuple([ int(num) for num in __version__.split('.')])
__copyright__ = '(c) Scale GmbH'


import os
import sys
import time
import pandas as pd
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from numpy import arange, sin, pi
from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

class Measurement(object):
    def __init__(self, filepath):
        self.df = None
        self.X = None
        self.Y = None
        self.Z = None
        self.read_df(filepath)
        self.filepath = filepath

    def read_df(self, filepath):
    
        df = pd.read_csv(os.path.join(filepath), header=None, sep="\t", decimal=",")
        df.drop(157, axis=1, inplace=True)
        print df.head()
        df.replace(-1, np.nan, inplace=True)
        zmin, zmax =  np.nanmin(df.values), np.nanmax(df.values)
        self.zmin, self.zmax =  np.nanmin(df.values), np.nanmax(df.values)
        
        df.replace(np.nan, 0, inplace=True)
    
        nx = len(df.columns)
        ny = len(df.index)
        xi = np.arange(nx)
        yi = np.arange(ny)
        x = np.linspace(0,2.,nx)
        y = np.linspace(0,1.,ny)
        # print x,y
        Xi, Yi = np.meshgrid(xi, yi)
        X, Y = np.meshgrid(x, y)
        # print X.shape
        # print Y.shape
        Z = np.zeros((ny,nx))
        # print Z.shape
        
        # print "!", df.shape
        for s in range(nx):
            for z in range(ny):
        #         print s, z, X[z,s],Y[z,s], df.loc[(Y[z,s],X[z,s])]
        #         print z,s, df.loc[(Y[z,s],X[z,s])]
        
                Z[z,s] = df.loc[(Yi[z,s],Xi[z,s])]

        self.df = df
        self.X = X
        self.Y = Y
        self.Z = Z

class SubPlotCanvas(FigureCanvas):

    def __init__(self, parent=None):
        self.initFigures()

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.__init__(self, self.figm)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    
    def initFigures(self):
        workpath = "/home/peter.keller/projects/pyQtTest/ingolf/amepa/"
        files = [x for x in os.listdir(workpath) if x.endswith(".txt") and "o_Oel" in x]
    
    	ms = []
    
    	for filename in files:
        	m = Measurement(os.path.join(workpath, filename))
        	ms.append(m)

		self.fig, self.axs = plt.subplots(len(ms), 1, dpi=150, facecolor='w', edgecolor='k', figsize=(200./25.4, 100./25.4), num="Drypro %s" % time.time(), sharex=True, sharey=True)
        self.figm, self.axm = plt.subplots(3, 1, dpi=150, facecolor='w', edgecolor='k', figsize=(200./25.4, 100./25.4), num="Drypro %s" % time.time(), sharex=True, sharey=True)
        zmean = np.zeros_like(ms[0].Z)
    	zmin = np.zeros_like(ms[0].Z) +100
    	zmax = np.zeros_like(ms[0].Z) -100

        for mi, m in enumerate(ms): 
		    zmean += m.Z
		    zmaxmask = zmax < m.Z
		    zmax[zmaxmask] = m.Z[zmaxmask]
		    zminmask = zmin > m.Z
		    zmin[zminmask] = m.Z[zminmask]

        vmin = zmin.min()
        vmax = zmin.max()

        print "vmin %.3f" % vmin
        print "vmax %.3f" % vmax
        for mi, m in enumerate(ms): 
		    self.axs[mi].text(0.0, 1.0, '%s' % os.path.split(m.filepath)[-1],
		        horizontalalignment='left',
		        verticalalignment='bottom',
		        transform=self.axs[mi].transAxes,
		        fontsize="x-small")
		    CS = self.axs[mi].contourf(m.X,m.Y,m.Z,50,cmap=plt.cm.rainbow, vmin=vmin, vmax=vmax)
		    df2 = m.df +m.df
		    print df2.shape
        self.fig.subplots_adjust(right=0.8)
        cbar_axm = self.fig.add_axes([0.85, 0.15, 0.05, 0.7])
        self.fig.colorbar(CS, cax=cbar_axm)
		
        zmean /= len(ms)

        CSmean = self.axm[0].contourf(m.X,m.Y,zmean,50,cmap=plt.cm.rainbow, vmin=vmin, vmax=vmax)
        CSmin = self.axm[1].contourf(m.X,m.Y,zmin,50,cmap=plt.cm.rainbow, vmin=vmin, vmax=vmax)
        CSmax = self.axm[2].contourf(m.X,m.Y,zmax,50,cmap=plt.cm.rainbow, vmin=vmin, vmax=vmax)
        self.axm[0].text(0.0, 1.0, 'mean',
		    horizontalalignment='left',
		    verticalalignment='bottom',
		    transform=self.axm[0].transAxes,
		    fontsize="x-small")
        self.axm[1].text(0.0, 1.0, 'min',
		    horizontalalignment='left',
		    verticalalignment='bottom',
		    transform=self.axm[1].transAxes,
		    fontsize="x-small")
        self.axm[2].text(0.0, 1.0, 'max',
		    horizontalalignment='left',
		    verticalalignment='bottom',
		    transform=self.axm[2].transAxes,
		    fontsize="x-small")

        self.figm.subplots_adjust(right=0.8)
        cbar_ax = self.figm.add_axes([0.85, 0.15, 0.05, 0.7])
        self.figm.colorbar(CS, cax=cbar_ax)

		
        self.figm.savefig("amepa.png")
        #plt.show()

class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.main_widget = QWidget(self)

        l = QVBoxLayout(self.main_widget)

        sc = SubPlotCanvas(self.main_widget)

        l.addWidget(sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("First Test Amepa MatplotLib", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()


if __name__ == '__main__':
    

    #print ms
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 Matplot Example")
    aw.show()
    #sys.exit(qApp.exec_())

    app.exec_()
