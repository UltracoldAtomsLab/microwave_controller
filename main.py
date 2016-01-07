import sys

import serial
import serial.tools.list_ports
from PyQt4.QtGui import *

from mainwindow import Ui_mainWindow
from util import *

template = "t0 {index:04x} {freq0:08x},{phase0:04x},{amp0:04x},{time:02x}\nt1 {index:04x} {freq1:08x},{phase1:04x},{amp1:04x},{time:02x}\n"
WAIT_TRIG = 255
emptyConfig = '''{
"portPTS" : None,
"portNova" : None,
}'''


class main(QMainWindow, Ui_mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # serial port initialization PTS
        self.serPTS = serial.Serial()
        self.serPTS.setBaudrate(115200)
        self.serPTS.setStopbits(2)
        self.refreshPTS()
        #seriral port initialization Novatech
        self.serNova = serial.Serial()
        self.serNova.setBaudrate(19200)
        self.serNova.setStopbits(2)
        self.refreshNova()
        # link buttons PTS
        self.pushButton_PTSrefresh.clicked.connect(self.refreshPTS)
        self.pushButton_SET_PTS.clicked.connect(self.setPTS)
        #link buttons Novatech
        self.pushButton_Novarefresh.clicked.connect(self.refreshNova)
        self.pushButton_SET_Nova.clicked.connect(self.setNova)

        self.load_config()


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

            Novaf0i = int(float(self.lineEdit_Novaf0i.displayText())*10)
            Novaf0d = int(float(self.lineEdit_Novaf0d.displayText())*10)
            Novaf1i = int(float(self.lineEdit_Novaf1i.displayText())*10)
            Novaf1d = int(float(self.lineEdit_Novaf1d.displayText())*10)
            NovaA0i = int(float(self.lineEdit_NovaA0i.displayText())*1023)
            NovaA0d = int(float(self.lineEdit_NovaA0d.displayText())*1023)
            NovaA1i = int(float(self.lineEdit_NovaA0i.displayText())*1023)
            NovaA1d = int(float(self.lineEdit_NovaA0d.displayText())*1023)
            Novap0i = int(float(self.lineEdit_Novap0i.displayText())*8192)
            Novap0d = int(float(self.lineEdit_Novap0d.displayText())*8192)
            Novap1i = int(float(self.lineEdit_Novap1i.displayText())*8192)
            Novap1d = int(float(self.lineEdit_Novap1d.displayText())*8192)

            to_write = "m 0\n"
            for i in range(loop):
                to_write += template.format(index=i, time=WAIT_TRIG,
                                            freq0=Novaf0i + i * Novaf0d, phase0=Novap0i + i * Novap0d,
                                            amp0=NovaA0i + i * NovaA0d,
                                            freq1=Novaf1i + i * Novaf1d, phase1=Novap1i + i * Novap1d,
                                            amp1=NovaA1i + i * NovaA1d, )
            to_write += 'm t\n'
            print to_write
            self.serNova.write(to_write)
        except Exception as err:
            QMessageBox.about(self, "ERROR", str(err))
            return

    def load_config(self):
        try:
            s = open('config.txt', 'r').read()
            d = eval(s)
        except IOError:
            with open("config.txt", 'w') as f:
                f.write(emptyConfig)

        try:
            p = self.comboBox_port_list_PTS.findText(str(d["portPTS"]))
            self.comboBox_port_list_PTS.setCurrentIndex(p)
        except Exception:
            pass

        try:
            p = self.comboBox_port_list_Nova.findText(str(d["portNova"]))
            self.comboBox_port_list_Nova.setCurrentIndex(p)
        except Exception:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainprogram = main()
    mainprogram.show()
    sys.exit(app.exec_())