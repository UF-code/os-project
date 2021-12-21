from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5 import uic
import sys, psutil, time
from hurry.filesize import size


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(60, 80, 331, 261))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(420, 80, 321, 261))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 420, 201, 81))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.thread={}
        self.cpu_list=[]
        self.ram_list=[]
        self.counter_list=[]
        self.pushButton.clicked.connect(self.cpu_worker_1)

    def cpu_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)
    
    def my_function(self, counter, cpu_, ram_):
        # index = self.sender().index
        index = 1
        self.graphicsView.clear()
        if index == 1:
        # cpu_ =psutil.cpu_percent(interval=1)
            self.counter_list.append(counter)
            self.cpu_list.append(cpu_)
            self.ram_list.append(ram_)
            # print(self.counter_list)
            # print(self.cpu_list)
            self.graphicsView.plot(self.counter_list, self.cpu_list, pen='r', name='CPU')
            
            
            self.graphicsView_2.plot(self.counter_list, self.ram_list, pen='g', name='RAM')
        # if index == 2:

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class ThreadClass(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int, float, float)
    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index=index
    def run(self):
        counter = 0
        while True:
            counter+=1
            time.sleep(0.01)
            ram_ = psutil.virtual_memory().percent
            cpu_ =psutil.cpu_percent(interval=1)
            self.any_signal.emit(counter, cpu_, ram_)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
