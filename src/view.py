import matplotlib
import numpy as np
from PyQt5.QtCore import QObjectCleanupHandler

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from mplwidget import MainWindow
from presenter import presenter_calc


class Ui_View(QtWidgets.QMainWindow):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(634, 766)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View.sizePolicy().hasHeightForWidth())
        View.setSizePolicy(sizePolicy)
        View.setMinimumSize(QtCore.QSize(634, 766))
        View.setMaximumSize(QtCore.QSize(634, 766))
        self.centralwidget = QtWidgets.QWidget(View)
        self.centralwidget.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: #BA55D3;")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_lbr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lbr.setGeometry(QtCore.QRect(340, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_lbr.setFont(font)
        self.pushButton_lbr.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_lbr.setObjectName("pushButton_lbr")
        self.pushButton_rbr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rbr.setGeometry(QtCore.QRect(410, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_rbr.setFont(font)
        self.pushButton_rbr.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_rbr.setObjectName("pushButton_rbr")
        self.pushButton_pow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pow.setGeometry(QtCore.QRect(480, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_pow.setFont(font)
        self.pushButton_pow.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_pow.setObjectName("pushButton_pow")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(550, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 135, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 135, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 135, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(550, 135, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_mult = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mult.setGeometry(QtCore.QRect(550, 200, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mult.setFont(font)
        self.pushButton_mult.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 265, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 265, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(340, 265, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("\n"
"border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(550, 265, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(340, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(550, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(480, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(410, 330, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_sin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sin.setGeometry(QtCore.QRect(20, 70, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.pushButton_cos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cos.setGeometry(QtCore.QRect(120, 70, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.pushButton_tan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tan.setGeometry(QtCore.QRect(220, 70, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_tan.setFont(font)
        self.pushButton_tan.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_tan.setObjectName("pushButton_tan")
        self.pushButton_acos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_acos.setGeometry(QtCore.QRect(120, 135, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_acos.setFont(font)
        self.pushButton_acos.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_acos.setObjectName("pushButton_acos")
        self.pushButton_atan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atan.setGeometry(QtCore.QRect(220, 135, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_atan.setFont(font)
        self.pushButton_atan.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_atan.setObjectName("pushButton_atan")
        self.pushButton_asin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_asin.setGeometry(QtCore.QRect(20, 135, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_asin.setFont(font)
        self.pushButton_asin.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_asin.setObjectName("pushButton_asin")
        self.pushButton_ln = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ln.setGeometry(QtCore.QRect(120, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_ln.setFont(font)
        self.pushButton_ln.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.pushButton_log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log.setGeometry(QtCore.QRect(220, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_log.setFont(font)
        self.pushButton_log.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_log.setObjectName("pushButton_log")
        self.pushButton_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sqrt.setGeometry(QtCore.QRect(20, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_sqrt.setFont(font)
        self.pushButton_sqrt.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.pushButton_e = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_e.setGeometry(QtCore.QRect(20, 265, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_e.setFont(font)
        self.pushButton_e.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_e.setObjectName("pushButton_e")
        self.pushButton_mod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mod.setGeometry(QtCore.QRect(120, 265, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_mod.setFont(font)
        self.pushButton_mod.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.pushButton_graphic = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_graphic.setGeometry(QtCore.QRect(420, 430, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_graphic.setFont(font)
        self.pushButton_graphic.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_graphic.setObjectName("pushButton_graphic")
        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_history.setGeometry(QtCore.QRect(220, 265, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_history.setObjectName("pushButton_history")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 530, 41, 41))
        self.label.setStyleSheet("background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.Xmin = QtWidgets.QLineEdit(self.centralwidget)
        self.Xmin.setGeometry(QtCore.QRect(500, 520, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Xmin.setFont(font)
        self.Xmin.setStyleSheet("background: white;")
        self.Xmin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Xmin.setObjectName("Xmin")
        self.Xmax = QtWidgets.QLineEdit(self.centralwidget)
        self.Xmax.setGeometry(QtCore.QRect(500, 560, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Xmax.setFont(font)
        self.Xmax.setStyleSheet("background: white;")
        self.Xmax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Xmax.setObjectName("Xmax")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(440, 630, 41, 41))
        # self.label_2.setStyleSheet("background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        # self.label_2.setObjectName("label_2")
        # self.Ymin = QtWidgets.QLineEdit(self.centralwidget)
        # self.Ymin.setGeometry(QtCore.QRect(500, 620, 111, 21))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.Ymin.setFont(font)
        # self.Ymin.setStyleSheet("background: white;")
        # self.Ymin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.Ymin.setObjectName("Ymin")
        # self.Ymax = QtWidgets.QLineEdit(self.centralwidget)
        # self.Ymax.setGeometry(QtCore.QRect(500, 660, 113, 21))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.Ymax.setFont(font)
        # self.Ymax.setStyleSheet("background: white;")
        # self.Ymax.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.Ymax.setObjectName("Ymax")
        self.pushButton_x = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_x.setGeometry(QtCore.QRect(20, 340, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_x.setFont(font)
        self.pushButton_x.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_x.setObjectName("pushButton_x")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 601, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(255)
        self.lineEdit_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x.setGeometry(QtCore.QRect(120, 350, 81, 31))
        self.lineEdit_x.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_x.setReadOnly(True)
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.pushButton_info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_info.setGeometry(QtCore.QRect(530, 430, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_info.setFont(font)
        self.pushButton_info.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_info.setObjectName("pushButton_info")
        self.pushButton_clear_his = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_his.setGeometry(QtCore.QRect(220, 340, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.pushButton_clear_his.setFont(font)
        self.pushButton_clear_his.setStyleSheet("border-radius: 7px;\n"
"border-color: #f44336;\n"
"color: black;\n"
"border: 2px solid #4B0082;\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:reflect, x1:0, y1:0, x2:0.507, y2:0.489, stop:0 rgba(227, 129, 255, 255), stop:0.985222 rgba(255, 255, 255, 255));")
        self.pushButton_clear_his.setObjectName("pushButton_clear_his")
        self.widget_gr = QtWidgets.QWidget(self.centralwidget)
        self.widget_gr.setGeometry(QtCore.QRect(20, 420, 391, 331))
        self.widget_gr.setObjectName("widget_gr")
        self.widget_gr.setLayout(QtWidgets.QVBoxLayout())
        View.setCentralWidget(self.centralwidget)

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

        ####
        self.add_function()
        ####

    def retranslateUi(self, View):
        _translate = QtCore.QCoreApplication.translate
        View.setWindowTitle(_translate("View", "SmartCalc"))
        self.lineEdit.setFocus()
        self.pushButton_lbr.setText(_translate("View", "("))
        self.pushButton_rbr.setText(_translate("View", ")"))
        self.pushButton_pow.setText(_translate("View", "^"))
        self.pushButton_clear.setText(_translate("View", "AC"))
        self.pushButton_9.setText(_translate("View", "9"))
        self.pushButton_8.setText(_translate("View", "8"))
        self.pushButton_7.setText(_translate("View", "7"))
        self.pushButton_div.setText(_translate("View", "/"))
        self.pushButton_6.setText(_translate("View", "6"))
        self.pushButton_5.setText(_translate("View", "5"))
        self.pushButton_4.setText(_translate("View", "4"))
        self.pushButton_mult.setText(_translate("View", "*"))
        self.pushButton_3.setText(_translate("View", "3"))
        self.pushButton_2.setText(_translate("View", "2"))
        self.pushButton_1.setText(_translate("View", "1"))
        self.pushButton_minus.setText(_translate("View", "-"))
        self.pushButton_dot.setText(_translate("View", "."))
        self.pushButton_plus.setText(_translate("View", "+"))
        self.pushButton_equal.setText(_translate("View", "="))
        self.pushButton_0.setText(_translate("View", "0"))
        self.pushButton_sin.setText(_translate("View", "sin"))
        self.pushButton_cos.setText(_translate("View", "cos"))
        self.pushButton_tan.setText(_translate("View", "tan"))
        self.pushButton_acos.setText(_translate("View", "acos"))
        self.pushButton_atan.setText(_translate("View", "atan"))
        self.pushButton_asin.setText(_translate("View", "asin"))
        self.pushButton_ln.setText(_translate("View", "ln"))
        self.pushButton_log.setText(_translate("View", "log"))
        self.pushButton_sqrt.setText(_translate("View", "sqrt"))
        self.pushButton_e.setText(_translate("View", "E"))
        self.pushButton_mod.setText(_translate("View", "%"))
        self.pushButton_graphic.setText(_translate("View", "Graphic"))
        self.pushButton_history.setText(_translate("View", "History"))
        self.label.setText(_translate("View", "   X"))
        self.Xmin.setText(_translate("View", "-10"))
        self.Xmax.setText(_translate("View", "10"))
        # self.label_2.setText(_translate("View", "   Y"))
        # self.Ymin.setText(_translate("View", "-10"))
        # self.Ymax.setText(_translate("View", "10"))
        self.pushButton_x.setText(_translate("View", "x"))
        self.pushButton_info.setText(_translate("View", "INFO"))
        self.pushButton_clear_his.setText(_translate("View", "Clear\n"
"History"))


    def add_function(self):
        self.pushButton_0.clicked.connect(lambda:self.write_button(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda:self.write_button(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.write_button(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_button(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_button(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.write_button(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.write_button(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.write_button(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.write_button(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_button(self.pushButton_9.text()))
        self.pushButton_lbr.clicked.connect(lambda: self.write_button(self.pushButton_lbr.text()))
        self.pushButton_rbr.clicked.connect(lambda: self.write_button(self.pushButton_rbr.text()))
        self.pushButton_pow.clicked.connect(lambda: self.write_button(self.pushButton_pow.text()))
        self.pushButton_div.clicked.connect(lambda: self.write_button(self.pushButton_div.text()))
        self.pushButton_mult.clicked.connect(lambda: self.write_button(self.pushButton_mult.text()))
        self.pushButton_minus.clicked.connect(lambda: self.write_button(self.pushButton_minus.text()))
        self.pushButton_dot.clicked.connect(lambda: self.write_button(self.pushButton_dot.text()))
        self.pushButton_plus.clicked.connect(lambda: self.write_button(self.pushButton_plus.text()))
        self.pushButton_sin.clicked.connect(lambda: self.write_button(self.pushButton_sin.text() + "("))
        self.pushButton_cos.clicked.connect(lambda: self.write_button(self.pushButton_cos.text()+ "("))
        self.pushButton_tan.clicked.connect(lambda: self.write_button(self.pushButton_tan.text()+ "("))
        self.pushButton_acos.clicked.connect(lambda: self.write_button(self.pushButton_acos.text()+ "("))
        self.pushButton_atan.clicked.connect(lambda: self.write_button(self.pushButton_atan.text()+ "("))
        self.pushButton_asin.clicked.connect(lambda: self.write_button(self.pushButton_asin.text()+ "("))
        self.pushButton_ln.clicked.connect(lambda: self.write_button(self.pushButton_ln.text()))
        self.pushButton_log.clicked.connect(lambda: self.write_button(self.pushButton_log.text()))
        self.pushButton_sqrt.clicked.connect(lambda: self.write_button(self.pushButton_sqrt.text()))
        self.pushButton_e.clicked.connect(lambda: self.write_button(self.pushButton_e.text()))
        self.pushButton_mod.clicked.connect(lambda: self.write_button(self.pushButton_mod.text()))
        self.pushButton_x.clicked.connect(lambda: self.write_button(self.pushButton_x.text()))
        self.pushButton_equal.clicked.connect(self.results)
        self.pushButton_clear.clicked.connect(lambda: self.clear_all(self.widget_gr.layout()))
        self.pushButton_clear_his.clicked.connect(lambda: self.clear_history())
        self.pushButton_history.clicked.connect(lambda: self.load_history())
        self.pushButton_graphic.clicked.connect(self.update_graph)
        self.pushButton_info.clicked.connect(lambda: self.get_info())

    def update_graph(self):
        str_history = self.lineEdit.text()
        with open("history.txt", "a+") as file_object:
            file_object.seek(0)
            file_object.write(str_history)
            file_object.write("\n")
        if "x" in self.lineEdit.text():
            if self.is_number1(self.Xmin.text()) and self.is_number1(self.Xmax.text()):
                    xmi = int(self.Xmin.text())
                    xma = int(self.Xmax.text())
                    values_x = np.arange(xmi, xma, 0.1)
                    values_y =[]
                    for i in values_x:
                        values_y.append(presenter_calc(self.lineEdit.text(), i))
                    if 2024.20242024 in values_y:
                        self.lineEdit.setText("Err")
                    else:
                        sc = MainWindow(values_x, values_y)
                        toolbar = NavigationToolbar(sc, self)
                        QObjectCleanupHandler().add(self.widget_gr.layout())
                        layout = QtWidgets.QVBoxLayout()
                        layout.addWidget(toolbar)
                        layout.addWidget(sc)
                        self.widget_gr.setLayout(layout)
    def write_button(self, num):
        if self.lineEdit.hasFocus():
            self.lineEdit.setText(self.lineEdit.text() + num)
            self.lineEdit.setFocus()
        else:
            self.lineEdit_x.setText(self.lineEdit_x.text() + num)
            self.lineEdit_x.setFocus()

    def results(self):
        str_history = self.lineEdit.text()
        with open("history.txt", "a+") as file_object:
                file_object.seek(0)
                file_object.write(str_history)
                file_object.write("\n")

        if len(self.lineEdit.text()) != 0:
           if ("x" in self.lineEdit.text() and len(self.lineEdit_x.text()) != 0) or ("x" not in self.lineEdit.text() and len(self.lineEdit_x.text()) == 0):
                res = 0
                if len(self.lineEdit_x.text()) == 0:
                    val_x = 1
                    res = presenter_calc(self.lineEdit.text(), val_x)
                else:
                    if self.is_number1(self.lineEdit_x.text()) == True:
                        val_x = float(self.lineEdit_x.text())
                        res = presenter_calc(self.lineEdit.text(), val_x)
                    else:
                        self.lineEdit_x.setText("Err")
                        self.lineEdit.setText("Err")
                if res == 2024.20242024:
                   self.lineEdit.setText("Err")
                elif self.lineEdit.text() != "Err":
                    self.lineEdit.setText(str(res))
           else:
                info = QMessageBox()
                info.setText("Введите валидное значение для Х")
                info.setIcon(QMessageBox.Information)
                info.setStandardButtons(QMessageBox.Close)
                info.exec_()

    def is_number1(self, s: str):
        try:
            float(s)
            return True
        except ValueError:
            return False
    def clear_all(self, layout):
        self.lineEdit.clear()
        self.lineEdit_x.clear()
        for i in reversed(range(layout.count())):
            if layout.itemAt(i).widget():
                layout.itemAt(i).widget().setParent(None)
            else:
                layout.removeItem(layout.itemAt(i))

    def load_history(self):
        # self.clear_all(self.widget_gr.layout())
        self.lineEdit.clear()
        with open('history.txt', 'r+') as f:
            lines = f.readlines()
            if len(lines) > 0:
                load_str = lines.pop()
                self.lineEdit.setText(load_str[:-1])
                f.truncate(0)

        with open('history.txt', 'w') as f:
            f.writelines(lines)

    def clear_history(self):
        with open('history.txt', 'r+') as f:
            f.truncate(0)

    def get_info(self):
        info = QMessageBox()
        info.setWindowTitle("Информация")
        info.setText("""        Расширенная версия обычного калькулятора, который можно найти в стандартных приложениях каждой операционной системы.
            Помимо базовых арифметических операций, как плюс-минус и умножить-поделить, калькулятор имеет возможность вычисления арифметических выражений с учетом приоритетов, а так же некоторых математических функций (синус, косинус, логарифм и т.д.).
            Помимо вычисления выражений калькулятор так же поддерживает использование переменной x и построение графика соответствующей функции.
""")
        info.setIcon(QMessageBox.Information)
        info.setStandardButtons(QMessageBox.Close)
        info.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    View = QtWidgets.QMainWindow()
    ui = Ui_View()
    ui.setupUi(View)
    View.show()
    sys.exit(app.exec_())
