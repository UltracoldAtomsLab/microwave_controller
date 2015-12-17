import sys
from PyQt4.QtGui import *
from mainwindow import Ui_mainWindow
import serial
import serial.tools.list_ports
from util import *

template = "t0 {index} {freq0},{phase0},{amp0},{time}\nt1 {index} {freq1},{phase1},{amp1},{time}\n"

class main(QMainWindow, Ui_mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # serial port initialization PTS
        self.serPTS = serial.Serial()
        self.serPTS.setBaudrate(115200)                                         """HOW to decide Baudrate!!?"""
        self.serPTS.setStopbits(2)
        self.refreshPTS()
        #seriral port initialization Novatech
        self.serNova = serial.Serial()
        self.serNova.setBaudrate(19200)                                         """HOW to decide Baudrate!!?"""
        self.serNova.setStopbits(2)
        self.refreshNova()
        # link buttons PTS
        self.pushButton_PTSrefresh.clicked.connect(self.refreshPTS)
        self.pushButton_SET_PTS.clicked.connect(self.setPTS)
        #link buttons Novatech
        self.pushButton_Novarefresh.clicked.connect(self.refreshNova)
        """self.pushButton_SET_Nova.clicked.connect(self.setNova)"""

    def refreshPTS(self):
        self.comboBox_port_list_PTS.clear()
        port_list = [i[0] for i in list(serial.tools.list_ports.comports())]
        self.comboBox_port_list_PTS.addItems(port_list)

        
    def setPTS(self):
        try:
            port = str(self.comboBox_port_list_PTS.currentText())
            self.serPTS.setPort(port)
            if not self.serPTS.isOpen():
                self.serPTS.open()
            loop = int(self.spinBox_PTS.value())
            # divided by 100 because we only modify the frequency to 100Hz

            PTSf1i = transform(self.lineEdit_PTSf1i.displayText())
            PTSf1d = transform(self.lineEdit_PTSf1d.displayText())
            PTSf2i = transform(self.lineEdit_PTSf2i.displayText())
            PTSf2d = transform(self.lineEdit_PTSf2d.displayText())
            PTSf3i = transform(self.lineEdit_PTSf3i.displayText())
            PTSf3d = transform(self.lineEdit_PTSf3d.displayText())

            index = 0
            for i in range(loop):
                to_write = setFreq(index, PTSf1i + i * PTSf1d)
                print to_write
                self.serPTS.write(to_write)
                index += 1
                if self.checkBox_PTSf2.isChecked():
                    self.serPTS.write(setFreq(index, PTSf2i + i * PTSf2d))
                    index += 1
                if self.checkBox_PTSf3.isChecked():
                    self.serPTS.write(setFreq(index, PTSf3i + i * PTSf3d))
                    index += 1
            self.serPTS.write(setIndex(0))
        except Exception as err:
            QMessageBox.about(self, "ERROR", str(err))
            return
        print "done!"

    def refreshNova(self):
            self.comboBox_port_list_Nova.clear()
            port_list = [i[0] for i in list(serial.tools.list_ports.comports())]
            self.comboBox_port_list_Nova.addItems(port_list)

    def setNova(self):
        try:
            port = str(self.comboBox_port_list_Nova.currentText())
            self.serNova.setPort(port)
            if not self.serNova.isOpen():
                self.serNova.open()
            loop = int(self.spinBox_Nova.value())

        Novaf0i = int(self.lineEdit_Novaf0i)
        Novaf0d = int(self.lineEdit_Novaf0d)
        Novaf1i = int(self.lineEdit_Novaf1i)
        Novaf1d = int(self.lineEdit_Novaf1d)
        NovaA0i = int(self.lineEdit_NovaA0i)
        NovaA0d = int(self.lineEdit_NovaA0d)
        NovaA1i = int(self.lineEdit_NovaA0i)
        NovaA1d = int(self.lineEdit_NovaA0d)
        Novap0i = int(self.lineEdit_Novap0i)
        Novap0d = int(self.lineEdit_Novap0d)
        Novap1i = int(self.lineEdit_Novap1i)
        Novap1d = int(self.lineEdit_Novap1d)

        index = 0
        to_write = "m 0\n"
        for i in range(loop):
            to_write += template.format()
        to_write += template.format()
        to_write += 'm t\n'

        self.serNova(to_write)



app = QApplication(sys.argv)
mainprogram = main()
mainprogram.show()
sys.exit(app.exec_())