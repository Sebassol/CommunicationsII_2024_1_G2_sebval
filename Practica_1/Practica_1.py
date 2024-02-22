#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Practica 1
# GNU Radio version: 3.9.8.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import Practica_1_epy_block_2 as epy_block_2  # embedded python block



from gnuradio import qtgui

class Practica_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Practica 1", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Practica 1")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Practica_1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.epy_block_2 = epy_block_2.blk()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((1, 2, -1), True, 1, [])
        self.RMS = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.RMS.set_update_time(0.10)
        self.RMS.set_title("RMS")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.RMS.set_min(i, -1)
            self.RMS.set_max(i, 1)
            self.RMS.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.RMS.set_label(i, "Data {0}".format(i))
            else:
                self.RMS.set_label(i, labels[i])
            self.RMS.set_unit(i, units[i])
            self.RMS.set_factor(i, factor[i])

        self.RMS.enable_autoscale(False)
        self._RMS_win = sip.wrapinstance(self.RMS.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._RMS_win)
        self.POTENCIA_PROMEDIO = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.POTENCIA_PROMEDIO.set_update_time(0.10)
        self.POTENCIA_PROMEDIO.set_title("POTENCIA PROMEDIO")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.POTENCIA_PROMEDIO.set_min(i, -1)
            self.POTENCIA_PROMEDIO.set_max(i, 1)
            self.POTENCIA_PROMEDIO.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.POTENCIA_PROMEDIO.set_label(i, "Data {0}".format(i))
            else:
                self.POTENCIA_PROMEDIO.set_label(i, labels[i])
            self.POTENCIA_PROMEDIO.set_unit(i, units[i])
            self.POTENCIA_PROMEDIO.set_factor(i, factor[i])

        self.POTENCIA_PROMEDIO.enable_autoscale(False)
        self._POTENCIA_PROMEDIO_win = sip.wrapinstance(self.POTENCIA_PROMEDIO.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._POTENCIA_PROMEDIO_win)
        self.MEDIA_CUADRATICA = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.MEDIA_CUADRATICA.set_update_time(0.10)
        self.MEDIA_CUADRATICA.set_title("MEDIA CUADRATICA")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.MEDIA_CUADRATICA.set_min(i, -1)
            self.MEDIA_CUADRATICA.set_max(i, 1)
            self.MEDIA_CUADRATICA.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.MEDIA_CUADRATICA.set_label(i, "Data {0}".format(i))
            else:
                self.MEDIA_CUADRATICA.set_label(i, labels[i])
            self.MEDIA_CUADRATICA.set_unit(i, units[i])
            self.MEDIA_CUADRATICA.set_factor(i, factor[i])

        self.MEDIA_CUADRATICA.enable_autoscale(False)
        self._MEDIA_CUADRATICA_win = sip.wrapinstance(self.MEDIA_CUADRATICA.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._MEDIA_CUADRATICA_win)
        self.MEDIA = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.MEDIA.set_update_time(0.10)
        self.MEDIA.set_title("MEDIA")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.MEDIA.set_min(i, -1)
            self.MEDIA.set_max(i, 1)
            self.MEDIA.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.MEDIA.set_label(i, "Data {0}".format(i))
            else:
                self.MEDIA.set_label(i, labels[i])
            self.MEDIA.set_unit(i, units[i])
            self.MEDIA.set_factor(i, factor[i])

        self.MEDIA.enable_autoscale(False)
        self._MEDIA_win = sip.wrapinstance(self.MEDIA.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._MEDIA_win)
        self.DESVIACION_EST = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.DESVIACION_EST.set_update_time(0.10)
        self.DESVIACION_EST.set_title("DESVIACION ESTANDAR")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.DESVIACION_EST.set_min(i, -1)
            self.DESVIACION_EST.set_max(i, 1)
            self.DESVIACION_EST.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.DESVIACION_EST.set_label(i, "Data {0}".format(i))
            else:
                self.DESVIACION_EST.set_label(i, labels[i])
            self.DESVIACION_EST.set_unit(i, units[i])
            self.DESVIACION_EST.set_factor(i, factor[i])

        self.DESVIACION_EST.enable_autoscale(False)
        self._DESVIACION_EST_win = sip.wrapinstance(self.DESVIACION_EST.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._DESVIACION_EST_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.epy_block_2, 0))
        self.connect((self.epy_block_2, 4), (self.DESVIACION_EST, 0))
        self.connect((self.epy_block_2, 0), (self.MEDIA, 0))
        self.connect((self.epy_block_2, 1), (self.MEDIA_CUADRATICA, 0))
        self.connect((self.epy_block_2, 3), (self.POTENCIA_PROMEDIO, 0))
        self.connect((self.epy_block_2, 2), (self.RMS, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Practica_1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(top_block_cls=Practica_1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
