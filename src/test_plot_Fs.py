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
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QHBoxLayout, QSizePolicy, QMessageBox, QWidget
from PyQt5.QtGui import QPalette
from numpy import arange, sin, pi
import matplotlib
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas

class Measurement(object):
    def __init__(self, file_path):
        self._df = None
        self._s = None
        self._f = None
        #self._read_df(file_path)
	self._read_excel_df(file_path)

    def _read_df(self, file_path):
    
        if os.path.exists(file_path):
            self._df = pd.read_csv(file_path, header=None, skiprows=9, sep=",", names=["s", "F"])
            self._s = self._df["s"]
            self._f = self._df["F"]
        else:
            raise ValueError("File unknown: {0}".format(file_path))
    def _read_excel_df(self, file_path):
        pass
    
    def get_data(self):
        return self._df


class MatplotWidget(QWidget):

    def __init__(self, parent, projection=None):
        super(MatplotWidget, self).__init__(parent)

        self._canvas = FigureCanvas(
                matplotlib.figure.Figure(
                        figsize=(4, 3),
                        dpi=100,
                        frameon=False))

        self._axes = self.figure.add_subplot(111, projection=projection)
        self._axes.axis("off")

        layout = QVBoxLayout()
        self._hori_layout = QHBoxLayout()
        self._hori_layout.addStretch(stretch=1)

        layout.addLayout(self._hori_layout)
        layout.addWidget(self._canvas)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setBackgroundRole(QPalette.Base)
        self.setForegroundRole(QPalette.Text)
        self.setMinimumSize(400, 200)

    @property
    def canvas(self):
        """
        Liefert die Zeichenfläche.

        :return: Zeichenfläche
        :rtype: `FigureCanvas`
        """
        return self._canvas

    @property
    def figure(self):
        """
        Liefert die Abbildung.

        :return: Abbildung
        :rtype: `FigureCanvas.figure`
        """
        return self.canvas.figure

    def set_title(self, text, bold=True):
        """
        Setzt den Titel der Grafik.

        :param text: Titel der Grafik
        :type text: `str`
        :param bold: Entscheidung, ob fettgedruckt
        :type bold: `bool`
        """
        return self._axes.set_title(
                text,
                x=0.0,
                horizontalalignment="left",
                color=self.palette().color(self.foregroundRole()).name(),
                fontsize=8,
                weight="bold" if bold else None)

    def draw(self):
        """
        Funktion zum Zeichnen der Grafik-.
        """
        self.canvas.draw()

    def clear(self):
        """
        Funktion zum Zurücksetzen der Grafik.
        """
        self._axes.clear()
        self._axes.axis("off")


class VisualizationWidget(MatplotWidget):
    def __init__(self, measurement, parent=None):
        super(VisualizationWidget, self).__init__(parent)

        self._plot_source = None
        self.figure.xlabel = ""
        self.figure.ylabel = ""
        self._xlabel = ""
        self._ylabel = ""

        self._grid_enabled = True
        self._lines = []
        self._xmin = 0
        self._ymin = 0
        self._xmax = 1
        self._ymax = 1
        self._legend_location = 'upper left'
        self._data = measurement.get_data()

    def draw(self):
        """
        Funktion zum Zeichnen der Datenkurven der Versuchsserien.
        """
        self.reset_display_limits()
        self.clear()
        self._axes.axis("on")
        data = self._data
        line, = self._axes.plot(data["s"], data["F"], color="#FF0000", alpha=0.7, lw=0.7, ls="--")
        line.set_label("F-s")
        self._lines.append(line)

        self._axes.legend(loc=self._legend_location, fontsize='xx-small', framealpha=0.5, handlelength=4)
        self.figure.tight_layout(pad=0.1, h_pad=0, w_pad=0)
        self.canvas.draw()

    def set_axis_labels(self, xlabel, ylabel):
        """
        Setzt die Achsenbeschriftungen.

        :param xlabel: X-Achsenbeschriftung
        :type xlabel: `float`
        :param ylabel: Y-Achsenbeschriftung
        :type ylabel: `float`
        """
        self._xlabel = xlabel
        self._ylabel = ylabel

    def clear(self):
        """
        Setzt den Graphen zurück.
        """
        self._lines = []
        self._axes.clear()
        self._axes.axis("off")
        self._axes.grid(self._grid_enabled, alpha=0.2)
        self._axes.set_xlabel(self._xlabel, fontsize='x-small')
        self._axes.set_ylabel(self._ylabel, fontsize='x-small')
        self._axes.tick_params(labelsize='x-small')

        self._axes.set_xlim(left=self._xmin, right=self._xmax)
        self._axes.set_ylim(bottom=self._ymin, top=self._ymax)

    def reset_display_limits(self):
        self._xmin = max(0.0, self._data["s"].min())
        self._xmax = 1.05 * self._data["s"].max()
        self._ymin = max(0.0, self._data["F"].min())
        self._ymax = 1.05 * self._data["F"].max()

    def set_data(self, data):
        self._data = data

    def axes(self):
        """
        Liefert die Zeichnung.

        :return: Zeichnung
        :rtype: `FigureCanvas.figure.subplot`
        """
        return self._axes


class PlotWidget(QMainWindow):
    def __init__(self, measurement):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.main_widget = QWidget(self)

        layout = QVBoxLayout(self.main_widget)

        plot_view = VisualizationWidget(measurement)
        plot_view.draw()
        layout.addWidget(plot_view)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

if __name__ == '__main__':
    f = []
    root_path = "/method/fosta"
    for (dirpath, dirnames, filenames) in os.walk(root_path):
	for index, file_i in enumerate(filenames):
	    if file_i.endswith("xlsx"):
	        f.append(os.path.join(dirpath, file_i))
    measurement = Measurement(f[0])
    app = QApplication(sys.argv)

    aw = PlotWidget(measurement)
    aw.setWindowTitle("PyQt5 Matplot Example")
    aw.show()

    app.exec_()
    
    
