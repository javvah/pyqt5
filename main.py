from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5 import uic


import sys,time


G_Counter=0

class Javvah(QtWidgets.QMainWindow):

    def __init__(self):
        
        QtWidgets.QMainWindow.__init__(self)
        self.ui=uic.loadUi('mainPage.ui',self)
        self.resize(800,400)
        icon=QtGui.QIcon()        
        self.mutex=QtCore.QMutex()
        icon.addPixmap(QtGui.QPixmap("kalibre.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)  
        self.pushButton_8.setEnabled(False) 

        self.thread={}
        self.pushButton.clicked.connect(self.start_worker_1)
        self.pushButton_2.clicked.connect(self.start_worker_2)
        self.pushButton_3.clicked.connect(self.start_worker_3)
        self.pushButton_4.clicked.connect(self.stop_workers)
        self.pushButton_5.clicked.connect(self.mutx_on)
        self.pushButton_6.clicked.connect(self.stop_worker_1)
        self.pushButton_7.clicked.connect(self.stop_worker_2)
        self.pushButton_8.clicked.connect(self.stop_worker_3)
        



    def start_worker_1(self):
        self.thread[0]=ThreadClass(parent=None,index=1)
        self.thread[0].start()
        #self.start_worker2()
        self.thread[0].any_signal.connect(self.myfunction)         
        self.pushButton.setEnabled(False)
        self.pushButton_6.setEnabled(True)    

    def start_worker_2(self):
        self.thread[1]=ThreadClass(parent=None,index=2)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.myfunction)          
        self.pushButton_2.setEnabled(False)
        self.pushButton_7.setEnabled(True) 

    def start_worker_3(self):
        self.thread[2]=ThreadClass(parent=None,index=3)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.myfunction)         
        self.pushButton_3.setEnabled(False)
        self.pushButton_8.setEnabled(True)

    def stop_worker_1(self):        
        self.thread[0].stop()
        self.pushButton.setEnabled(True)
        self.pushButton_6.setEnabled(False)    
    
    def stop_worker_2(self):        
        self.thread[1].stop()
        self.pushButton_2.setEnabled(True)
        self.pushButton_7.setEnabled(False)

    def stop_worker_3(self):        
        self.thread[2].stop()
        self.pushButton_3.setEnabled(True)
        self.pushButton_8.setEnabled(False)     

    def stop_workers(self):        
        self.thread[0].stop()
        self.thread[1].stop()
        self.thread[2].stop()           
        self.pushButton.setEnabled(True)
        self.pushButton_1.setEnabled(True)  
        self.pushButton_2.setEnabled(True)
    
    def mutx_on(self):
        G_Counter=1    

    def myfunction(self,counter):        
        cnt=counter
        index=self.sender().index        
        if index==1:
            self.mutex.lock()
            G_Counter=1 
            self.mutex.unlock()                  
            self.ui.label.setText(str(cnt))
            self.ui.label_4.setText(str(G_Counter))                        
        if index==2:
            G_Counter=2
            self.ui.label_2.setText(str(cnt))
            self.ui.label_4.setText(str(G_Counter))             
        if index==3:
            
            G_Counter=3            
            self.ui.label_3.setText(str(cnt))
            self.ui.label_4.setText(str(G_Counter))
                 

    

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)
    def __init__(self,parent=None,index=0):
        super(ThreadClass,self).__init__(parent)
        self.index=index        
        self.is_running=True
       
    
    def run(self):
        print("Start Thread",self.index)
        cnt=0
        while True:
            try:
               cnt+=1             
               if cnt==99 : cnt=0               
               G_Counter=2
               time.sleep(0.5)
               self.any_signal.emit(cnt)
               


            except :
                print(str(KeyError)) 

    def stop(self):
        self.is_running=False
        print('Stop thread')
        self.terminate()

app=QtWidgets.QApplication(sys.argv)
mainWindow =Javvah()
mainWindow.show()
sys.exit(app.exec_())
