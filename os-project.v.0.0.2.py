from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import sys, psutil
from hurry.filesize import size

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1070, 911)
        self.graph_cpu = PlotWidget(Dialog)
        self.graph_cpu.setGeometry(QtCore.QRect(40, 80, 491, 311))
        self.graph_cpu.setObjectName("graph_cpu")
        self.cpu_list = []
        self.graph_ram = PlotWidget(Dialog)
        self.graph_ram.setGeometry(QtCore.QRect(550, 80, 491, 311))
        self.graph_ram.setObjectName("graph_ram")
        self.ram_list = []
        self.graph_disk = PlotWidget(Dialog)
        self.graph_disk.setGeometry(QtCore.QRect(40, 450, 491, 311))
        self.graph_disk.setObjectName("graph_disk")
        self.disk_list = []
        self.graph_battery = PlotWidget(Dialog)
        self.graph_battery.setGeometry(QtCore.QRect(550, 450, 491, 311))
        self.graph_battery.setObjectName("graph_battery")
        self.battery_list = []
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.worker())
        self.pushButton.setGeometry(QtCore.QRect(460, 810, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.hehehe = QtWidgets.QLabel(Dialog)
        self.hehehe.setGeometry(QtCore.QRect(430, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.hehehe.setFont(font)
        self.hehehe.setAlignment(QtCore.Qt.AlignCenter)
        self.hehehe.setObjectName("hehehe")
        self.cpu_label = QtWidgets.QLabel(Dialog)
        self.cpu_label.setGeometry(QtCore.QRect(140, 390, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.cpu_label.setFont(font)
        self.cpu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_label.setObjectName("cpu_label")
        self.cpu_label_2 = QtWidgets.QLabel(Dialog)
        self.cpu_label_2.setGeometry(QtCore.QRect(240, 390, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.cpu_label_2.setFont(font)
        self.cpu_label_2.setText("")
        self.cpu_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cpu_label_2.setObjectName("cpu_label_2")
        self.ram_label = QtWidgets.QLabel(Dialog)
        self.ram_label.setGeometry(QtCore.QRect(700, 390, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.ram_label.setFont(font)
        self.ram_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_label.setObjectName("ram_label")
        self.ram_label_2 = QtWidgets.QLabel(Dialog)
        self.ram_label_2.setGeometry(QtCore.QRect(790, 390, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.ram_label_2.setFont(font)
        self.ram_label_2.setText("")
        self.ram_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_label_2.setObjectName("ram_label_2")
        self.disk_label_2 = QtWidgets.QLabel(Dialog)
        self.disk_label_2.setGeometry(QtCore.QRect(240, 760, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.disk_label_2.setFont(font)
        self.disk_label_2.setText("")
        self.disk_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.disk_label_2.setObjectName("disk_label_2")
        self.disk_label = QtWidgets.QLabel(Dialog)
        self.disk_label.setGeometry(QtCore.QRect(150, 760, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.disk_label.setFont(font)
        self.disk_label.setAlignment(QtCore.Qt.AlignCenter)
        self.disk_label.setObjectName("disk_label")
        self.battery_label = QtWidgets.QLabel(Dialog)
        self.battery_label.setGeometry(QtCore.QRect(690, 760, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.battery_label.setFont(font)
        self.battery_label.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_label.setObjectName("battery_label")
        self.battery_label_2 = QtWidgets.QLabel(Dialog)
        self.battery_label_2.setGeometry(QtCore.QRect(830, 760, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.battery_label_2.setFont(font)
        self.battery_label_2.setText("")
        self.battery_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_label_2.setObjectName("battery_label_2")
        self.disk_label_3 = QtWidgets.QLabel(Dialog)
        self.disk_label_3.setGeometry(QtCore.QRect(330, 760, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.disk_label_3.setFont(font)
        self.disk_label_3.setText("")
        self.disk_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.disk_label_3.setObjectName("disk_label_3")
        self.battery_label_4 = QtWidgets.QLabel(Dialog)
        self.battery_label_4.setGeometry(QtCore.QRect(860, 820, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.battery_label_4.setFont(font)
        self.battery_label_4.setText("")
        self.battery_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_label_4.setObjectName("battery_label_4")
        self.battery_label_3 = QtWidgets.QLabel(Dialog)
        self.battery_label_3.setGeometry(QtCore.QRect(690, 820, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(19)
        self.battery_label_3.setFont(font)
        self.battery_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_label_3.setObjectName("battery_label_3")
        self.counter_list = []
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.thread={}
    
    def worker(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.draw)
        self.pushButton.setEnabled(False)

        
    def draw(self, counter, cpu_, ram_, disk, battery):
        
        disk_percent, disk_used = disk
        battery_percent, battery_plugged = battery
        
        self.graph_cpu.clear()
        self.graph_ram.clear()
        self.graph_disk.clear()
        self.graph_battery.clear()
        
        self.counter_list.append(counter)
        self.cpu_list.append(cpu_)
        self.ram_list.append(ram_)
        self.graph_cpu.plot(self.counter_list, self.cpu_list, pen='r', name='CPU')
        self.cpu_label_2.setText(f"{cpu_} %")
            
        self.graph_ram.plot(self.counter_list, self.ram_list, pen='g', name='RAM')
        self.ram_label_2.setText(f"{ram_} %")

        self.disk_label_2.setText(f"{disk_percent} %")
        self.disk_label_3.setText(f"{size(disk_used)}")
        self.disk_list.append(disk_percent)
        self.graph_disk.plot(self.counter_list, self.disk_list, pen='y', name='DISK')

        self.battery_label_2.setText(f"{battery_percent} %")
        self.battery_label_4.setText(f"{battery_plugged}")
        self.battery_list.append(battery_percent)
        self.graph_battery.plot(self.counter_list, self.battery_list, pen='c', name='BATTERY')
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.hehehe.setText(_translate("Dialog", "uf-code.com"))
        self.cpu_label.setText(_translate("Dialog", "CPU :"))
        self.ram_label.setText(_translate("Dialog", "RAM :"))
        self.disk_label.setText(_translate("Dialog", "DISK :"))
        self.battery_label.setText(_translate("Dialog", "BATTERY :"))
        self.battery_label_3.setText(_translate("Dialog", "PLUGGED_IN :"))


class ThreadClass(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int, float, float, tuple, tuple)
    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index=index
    def run(self):
        counter = 0
        while True:
            counter+=1
            ram_ = psutil.virtual_memory().percent
            cpu_ = psutil.cpu_percent(interval=1)
            battery_ = psutil.sensors_battery()
            battery_percent, battery_plugged = battery_.percent, battery_.power_plugged
            disk_ = psutil.disk_usage('/')
            disk_used, disk_percent = disk_.used, disk_.percent
            self.any_signal.emit(counter, cpu_, ram_, (disk_percent, disk_used), (battery_percent, battery_plugged))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
