#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     selectcol.py
   Description :
   Author :       yueyao
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'yueyao'

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QGuiApplication, QColor, QCursor
from PyQt5.QtWidgets import QWidget, QApplication

import ui_colorcatcher


class ColorCatcher(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_colorcatcher.Ui_ColorCatcher()
        self.ui.setupUi(self)
        self.ui.lineEditMark.setText("Press space to mark!")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.catch)
        self.timer.start(100)
        self.nowColor = None
        self.setCursor(Qt.CrossCursor)
        self.show()

    def catch(self):
        x = QCursor.pos().x()
        y = QCursor.pos().y()
        pixmap = QGuiApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, 1, 1)
        if not pixmap.isNull():
            image = pixmap.toImage()
            if not image.isNull():
                if (image.valid(0, 0)):
                    color = QColor(image.pixel(0, 0))
                    r, g, b, _ = color.getRgb()
                    self.nowColor = color
                    self.ui.lineEditMove.setText('(%d, %d, %d) %s' % (r, g, b, color.name().upper()))
                    self.ui.lineEditMove.setStyleSheet('QLineEdit{border:2px solid %s;}' % (color.name()))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.ui.lineEditMark.setText(self.ui.lineEditMove.text())
            self.ui.lineEditMark.setStyleSheet('QLineEdit{border:2px solid %s;}' % (self.nowColor.name()))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = ColorCatcher()
    mainWindow.show()
    sys.exit(app.exec_())