# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jan 07 16:52:23 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(689, 550)
        self.centralWidget = QtGui.QWidget(mainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 80, 611, 391))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 21, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_PTSf1d = QtGui.QLineEdit(self.tab)
        self.lineEdit_PTSf1d.setGeometry(QtCore.QRect(200, 100, 113, 20))
        self.lineEdit_PTSf1d.setObjectName(_fromUtf8("lineEdit_PTSf1d"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 220, 151, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_PTSf1i = QtGui.QLineEdit(self.tab)
        self.lineEdit_PTSf1i.setGeometry(QtCore.QRect(200, 70, 113, 20))
        self.lineEdit_PTSf1i.setObjectName(_fromUtf8("lineEdit_PTSf1i"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 151, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(330, 100, 21, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.checkBox_PTSf2 = QtGui.QCheckBox(self.tab)
        self.checkBox_PTSf2.setGeometry(QtCore.QRect(360, 130, 73, 16))
        self.checkBox_PTSf2.setObjectName(_fromUtf8("checkBox_PTSf2"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(310, 20, 41, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_SET_PTS = QtGui.QPushButton(self.tab)
        self.pushButton_SET_PTS.setGeometry(QtCore.QRect(510, 320, 75, 23))
        self.pushButton_SET_PTS.setObjectName(_fromUtf8("pushButton_SET_PTS"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(330, 190, 21, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(330, 130, 21, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_PTSf3d = QtGui.QLineEdit(self.tab)
        self.lineEdit_PTSf3d.setGeometry(QtCore.QRect(200, 220, 113, 20))
        self.lineEdit_PTSf3d.setObjectName(_fromUtf8("lineEdit_PTSf3d"))
        self.lineEdit_PTSf2d = QtGui.QLineEdit(self.tab)
        self.lineEdit_PTSf2d.setGeometry(QtCore.QRect(200, 160, 113, 20))
        self.lineEdit_PTSf2d.setObjectName(_fromUtf8("lineEdit_PTSf2d"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(20, 190, 131, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_PTSf3i = QtGui.QLineEdit(self.tab)
        self.lineEdit_PTSf3i.setGeometry(QtCore.QRect(200, 190, 113, 20))
        self.lineEdit_PTSf3i.setObjectName(_fromUtf8("lineEdit_PTSf3i"))
        self.comboBox_port_list_PTS = QtGui.QComboBox(self.tab)
        self.comboBox_port_list_PTS.setGeometry(QtCore.QRect(90, 20, 121, 22))
        self.comboBox_port_list_PTS.setObjectName(_fromUtf8("comboBox_port_list_PTS"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(330, 70, 21, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_PTSrefresh = QtGui.QPushButton(self.tab)
        self.pushButton_PTSrefresh.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.pushButton_PTSrefresh.setObjectName(_fromUtf8("pushButton_PTSrefresh"))
        self.checkBox_PTSf3 = QtGui.QCheckBox(self.tab)
        self.checkBox_PTSf3.setGeometry(QtCore.QRect(360, 190, 73, 16))
        self.checkBox_PTSf3.setObjectName(_fromUtf8("checkBox_PTSf3"))
        self.spinBox_PTS = QtGui.QSpinBox(self.tab)
        self.spinBox_PTS.setGeometry(QtCore.QRect(360, 20, 42, 22))
        self.spinBox_PTS.setMaximum(1000)
        self.spinBox_PTS.setProperty("value", 100)
        self.spinBox_PTS.setObjectName(_fromUtf8("spinBox_PTS"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(330, 220, 21, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 151, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_PTSf2i = QtGui.QLineEdit(self.tab)
        self.lineEdit_PTSf2i.setGeometry(QtCore.QRect(200, 130, 113, 20))
        self.lineEdit_PTSf2i.setObjectName(_fromUtf8("lineEdit_PTSf2i"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 421, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.comboBox_port_list_Nova = QtGui.QComboBox(self.tab_2)
        self.comboBox_port_list_Nova.setGeometry(QtCore.QRect(90, 20, 121, 22))
        self.comboBox_port_list_Nova.setObjectName(_fromUtf8("comboBox_port_list_Nova"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(310, 20, 41, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 20, 61, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pushButton_Novarefresh = QtGui.QPushButton(self.tab_2)
        self.pushButton_Novarefresh.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.pushButton_Novarefresh.setObjectName(_fromUtf8("pushButton_Novarefresh"))
        self.spinBox_Nova = QtGui.QSpinBox(self.tab_2)
        self.spinBox_Nova.setGeometry(QtCore.QRect(360, 20, 42, 22))
        self.spinBox_Nova.setMaximum(1000)
        self.spinBox_Nova.setProperty("value", 100)
        self.spinBox_Nova.setObjectName(_fromUtf8("spinBox_Nova"))
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(20, 60, 58, 15))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(20, 130, 81, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_24 = QtGui.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(20, 250, 58, 15))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(20, 280, 81, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_22 = QtGui.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(20, 210, 81, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(20, 180, 58, 15))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_26 = QtGui.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(330, 110, 101, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(330, 190, 58, 15))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(330, 280, 81, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(330, 220, 81, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(330, 140, 81, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(330, 260, 58, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(330, 70, 58, 15))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.lineEdit_Novaf0i = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novaf0i.setGeometry(QtCore.QRect(110, 100, 113, 22))
        self.lineEdit_Novaf0i.setObjectName(_fromUtf8("lineEdit_Novaf0i"))
        self.lineEdit_Novaf0d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novaf0d.setGeometry(QtCore.QRect(110, 130, 113, 22))
        self.lineEdit_Novaf0d.setObjectName(_fromUtf8("lineEdit_Novaf0d"))
        self.lineEdit_NovaA0i = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_NovaA0i.setGeometry(QtCore.QRect(110, 180, 113, 22))
        self.lineEdit_NovaA0i.setObjectName(_fromUtf8("lineEdit_NovaA0i"))
        self.lineEdit_NovaA0d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_NovaA0d.setGeometry(QtCore.QRect(110, 210, 113, 22))
        self.lineEdit_NovaA0d.setObjectName(_fromUtf8("lineEdit_NovaA0d"))
        self.lineEdit_Novap0i = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novap0i.setGeometry(QtCore.QRect(110, 250, 113, 22))
        self.lineEdit_Novap0i.setObjectName(_fromUtf8("lineEdit_Novap0i"))
        self.lineEdit_Novap0d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novap0d.setGeometry(QtCore.QRect(110, 280, 113, 22))
        self.lineEdit_Novap0d.setObjectName(_fromUtf8("lineEdit_Novap0d"))
        self.lineEdit_NovaA1i = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_NovaA1i.setGeometry(QtCore.QRect(450, 180, 113, 22))
        self.lineEdit_NovaA1i.setObjectName(_fromUtf8("lineEdit_NovaA1i"))
        self.lineEdit_Novap1i = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novap1i.setGeometry(QtCore.QRect(450, 250, 113, 22))
        self.lineEdit_Novap1i.setObjectName(_fromUtf8("lineEdit_Novap1i"))
        self.lineEdit_Novaf1d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novaf1d.setGeometry(QtCore.QRect(450, 130, 113, 22))
        self.lineEdit_Novaf1d.setObjectName(_fromUtf8("lineEdit_Novaf1d"))
        self.lineEdit_Novap1d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novap1d.setGeometry(QtCore.QRect(450, 280, 113, 22))
        self.lineEdit_Novap1d.setObjectName(_fromUtf8("lineEdit_Novap1d"))
        self.lineEdit_Novaf1i = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_Novaf1i.setGeometry(QtCore.QRect(450, 100, 113, 22))
        self.lineEdit_Novaf1i.setObjectName(_fromUtf8("lineEdit_Novaf1i"))
        self.lineEdit_NovaA1d = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_NovaA1d.setGeometry(QtCore.QRect(450, 210, 113, 22))
        self.lineEdit_NovaA1d.setObjectName(_fromUtf8("lineEdit_NovaA1d"))
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(280, 60, 20, 291))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_SET_Nova = QtGui.QPushButton(self.tab_2)
        self.pushButton_SET_Nova.setGeometry(QtCore.QRect(520, 330, 75, 23))
        self.pushButton_SET_Nova.setObjectName(_fromUtf8("pushButton_SET_Nova"))
        self.label_33 = QtGui.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(230, 100, 31, 20))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(230, 130, 31, 20))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(570, 100, 31, 20))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(570, 130, 31, 20))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(470, 10, 91, 21))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_38 = QtGui.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(230, 250, 31, 20))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.tab_2)
        self.label_39.setGeometry(QtCore.QRect(230, 280, 31, 20))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_40 = QtGui.QLabel(self.tab_2)
        self.label_40.setGeometry(QtCore.QRect(570, 250, 31, 20))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_41 = QtGui.QLabel(self.tab_2)
        self.label_41.setGeometry(QtCore.QRect(570, 280, 31, 20))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(430, 0, 211, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralWidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.checkBox = QtGui.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(130, 20, 61, 19))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_2.setGeometry(QtCore.QRect(200, 20, 85, 19))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 689, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        mainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(mainWindow)
        self.mainToolBar.setEnabled(True)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(mainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "PTS Controller - Rb", None))
        self.label_9.setText(_translate("mainWindow", "f1 initial", None))
        self.label_5.setText(_translate("mainWindow", "kHz", None))
        self.label_6.setText(_translate("mainWindow", "serial port:", None))
        self.lineEdit_PTSf1d.setText(_translate("mainWindow", "0", None))
        self.label_3.setText(_translate("mainWindow", "f2 initial", None))
        self.label_14.setText(_translate("mainWindow", "f3 delta", None))
        self.lineEdit_PTSf1i.setText(_translate("mainWindow", "682.8", None))
        self.label_11.setText(_translate("mainWindow", "f1 delta", None))
        self.label_12.setText(_translate("mainWindow", "kHz", None))
        self.checkBox_PTSf2.setText(_translate("mainWindow", "use?", None))
        self.label_10.setText(_translate("mainWindow", "loop:", None))
        self.pushButton_SET_PTS.setText(_translate("mainWindow", "SET", None))
        self.label_16.setText(_translate("mainWindow", "kHz", None))
        self.label_4.setText(_translate("mainWindow", "kHz", None))
        self.lineEdit_PTSf3d.setText(_translate("mainWindow", "0", None))
        self.lineEdit_PTSf2d.setText(_translate("mainWindow", "0", None))
        self.label_13.setText(_translate("mainWindow", "f3 initial", None))
        self.lineEdit_PTSf3i.setText(_translate("mainWindow", "682.8", None))
        self.label_8.setText(_translate("mainWindow", "kHz", None))
        self.pushButton_PTSrefresh.setText(_translate("mainWindow", "Refresh", None))
        self.checkBox_PTSf3.setText(_translate("mainWindow", "use?", None))
        self.label_15.setText(_translate("mainWindow", "kHz", None))
        self.label_2.setText(_translate("mainWindow", "f2 delta", None))
        self.lineEdit_PTSf2i.setText(_translate("mainWindow", "682.8", None))
        self.label_7.setText(_translate("mainWindow", "[NOTE] The SET comment can be used only at trigger = 0 (off).", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "PTS", None))
        self.label_17.setText(_translate("mainWindow", "loop:", None))
        self.label_18.setText(_translate("mainWindow", "serial port:", None))
        self.pushButton_Novarefresh.setText(_translate("mainWindow", "Refresh", None))
        self.label_19.setText(_translate("mainWindow", "Port 0", None))
        self.label_20.setText(_translate("mainWindow", "frequency", None))
        self.label_21.setText(_translate("mainWindow", "freq change", None))
        self.label_24.setText(_translate("mainWindow", "phase", None))
        self.label_25.setText(_translate("mainWindow", "phase change", None))
        self.label_22.setText(_translate("mainWindow", "amp change", None))
        self.label_23.setText(_translate("mainWindow", "amplitude", None))
        self.label_26.setText(_translate("mainWindow", "frequency", None))
        self.label_27.setText(_translate("mainWindow", "amplitude", None))
        self.label_28.setText(_translate("mainWindow", "phase change", None))
        self.label_29.setText(_translate("mainWindow", "amp change", None))
        self.label_30.setText(_translate("mainWindow", "freq change", None))
        self.label_31.setText(_translate("mainWindow", "phase", None))
        self.label_32.setText(_translate("mainWindow", "Port 1", None))
        self.lineEdit_Novaf0i.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novaf0d.setText(_translate("mainWindow", "0", None))
        self.lineEdit_NovaA0i.setText(_translate("mainWindow", "0", None))
        self.lineEdit_NovaA0d.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novap0i.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novap0d.setText(_translate("mainWindow", "0", None))
        self.lineEdit_NovaA1i.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novap1i.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novaf1d.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novap1d.setText(_translate("mainWindow", "0", None))
        self.lineEdit_Novaf1i.setText(_translate("mainWindow", "0", None))
        self.lineEdit_NovaA1d.setText(_translate("mainWindow", "0", None))
        self.pushButton_SET_Nova.setText(_translate("mainWindow", "SET", None))
        self.label_33.setText(_translate("mainWindow", "Hz", None))
        self.label_34.setText(_translate("mainWindow", "Hz", None))
        self.label_35.setText(_translate("mainWindow", "Hz", None))
        self.label_36.setText(_translate("mainWindow", "Hz", None))
        self.label_37.setText(_translate("mainWindow", "amp: 0~1", None))
        self.label_38.setText(_translate("mainWindow", "π", None))
        self.label_39.setText(_translate("mainWindow", "π", None))
        self.label_40.setText(_translate("mainWindow", "π", None))
        self.label_41.setText(_translate("mainWindow", "π", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Novatech", None))
        self.label.setText(_translate("mainWindow", "Chung-You Shih @ lab107 IAMS", None))
        self.commandLinkButton.setText(_translate("mainWindow", "SET ALL", None))
        self.checkBox.setText(_translate("mainWindow", "PTS", None))
        self.checkBox_2.setText(_translate("mainWindow", "Notatech", None))

