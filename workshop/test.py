from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5 import uic
import sys, psutil, time
from hurry.filesize import size


class Test_Threads(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('untitled.ui', self)

        self.thread={}
        self.cpu_list=[]
        self.counter_list=[]
        self.pushButton.clicked.connect(self.cpu_worker_1)

    def cpu_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)

    # def ram_worker_2(self):
    #     self.thread[2] = ThreadClass(parent=None, index=2)
    #     self.thread[2].start()
    #     self.thread[2].any_signal.connect(self.my_function)

    def my_function(self, counter):
        index = self.sender().index
        self.graphicsView.clear()
        if index == 1:
            cpu_ =psutil.cpu_percent(interval=1)
            self.counter_list.append(counter)
            self.cpu_list.append(cpu_)
            print(self.counter_list)
            print(self.cpu_list)
            self.graphicsView.plot(self.counter_list, self.cpu_list, pen='r', name='CPU')
        # if index == 2:
        #     ram_ = psutil.virtual_memory().percent
        #     self.graphicsView_2.plot(counter, ram_, pen='g', name='RAM')
        
class ThreadClass(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index=index
    def run(self):
        counter = 0
        while True:
            counter+=1
            time.sleep(0.01)
            self.any_signal.emit(counter)



    


app = QtWidgets.QApplication(sys.argv)
mainWindow = Test_Threads()
mainWindow.show()
sys.exit(app.exec_())