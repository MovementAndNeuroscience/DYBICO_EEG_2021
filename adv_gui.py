# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:26:06 2021
@author: dzn332
"""

# file ui_main.py
from PyQt5.QtWidgets import QMainWindow, QDialog 
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QApplication, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas




class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(600, 200, 750, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")  
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("pushButton1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1") 
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2") 
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setObjectName("pushButton3")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label3") 
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setObjectName("pushButton3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setObjectName("label4") 
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setObjectName("pushButton5")

        
        self.label.setGeometry(QtCore.QRect(25, 30, 50, 30))
        self.lineEdit.setGeometry(QtCore.QRect(75, 30, 100, 30))
        self.pushButton1.setGeometry(QtCore.QRect(195, 30, 200, 30))
        self.pushButton2.setGeometry(QtCore.QRect(195, 70, 200, 30))
        self.pushButton3.setGeometry(QtCore.QRect(195, 110, 200, 30))
        self.pushButton4.setGeometry(QtCore.QRect(195, 150, 200, 30))
        self.pushButton5.setGeometry(QtCore.QRect(195, 190, 200, 30))
        self.label1.setGeometry(QtCore.QRect(405, 30, 200, 30))
        self.label2.setGeometry(QtCore.QRect(405, 70, 200, 30))
        self.label3.setGeometry(QtCore.QRect(405, 110, 200, 30))
        self.label4.setGeometry(QtCore.QRect(405, 150, 200, 30))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DYBICO"))
        self.pushButton1.setText(_translate("MainWindow", "Create Log"))
        self.pushButton2.setText(_translate("MainWindow", "Run Maxforce Test"))
        self.pushButton3.setText(_translate("MainWindow", "Calculate Maxforce"))
        self.pushButton4.setText(_translate("MainWindow", "Run Experiment"))
        self.pushButton5.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Log ID:"))
        self.lineEdit.setText(_translate("MainWindow", "test"))


        self.label1.setText(_translate("MainWindow", " "))
        self.label2.setText(_translate("MainWindow", " "))
        self.label3.setText(_translate("MainWindow", " "))
        self.label4.setText(_translate("MainWindow", " "))

        
        

#%%
class Ui_Dialog1:
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.setGeometry(700,200,550,250)
        
        self.maxforceBox = QtWidgets.QWidget(Dialog1)
        self.maxforceBox.setObjectName("maxforceBox")
        self.maxforceBox.setWindowTitle("Calibrate Maxforce")
        
        self.label_mf0 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf0.setObjectName("label_mf0") 
        self.label_mf0.setText("Specify settings for maxforce testing:") 
        self.label_mf0.setGeometry(QtCore.QRect(25, 30, 350, 30))

        self.label_mf1 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf1.setObjectName("label_mf1")  
        self.lineEdit_mf1 = QtWidgets.QLineEdit(self.maxforceBox)
        self.lineEdit_mf1.setObjectName("lineEdit_mf1")       
    
        self.label_mf2 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf2.setObjectName("label_mf2")  
        self.lineEdit_mf2 = QtWidgets.QLineEdit(self.maxforceBox)
        self.lineEdit_mf2.setObjectName("lineEdit_mf2") 
    
        self.label_mf3 = QtWidgets.QLabel(self.maxforceBox)
        self.label_mf3.setObjectName("label_mf3")  
        self.lineEdit_mf3 = QtWidgets.QLineEdit(self.maxforceBox)
        self.lineEdit_mf3.setObjectName("lineEdit_mf3") 
    
    
        self.label_mf1.setText("Trial duration: [seconds]") 
        self.lineEdit_mf1.setText("2") 
        self.label_mf1.setGeometry(QtCore.QRect(25, 70, 200, 30))
        self.lineEdit_mf1.setGeometry(QtCore.QRect(225, 70, 100, 30))
        
        self.label_mf2.setText("Scaling:") 
        self.lineEdit_mf2.setText("500") 
        self.label_mf2.setGeometry(QtCore.QRect(25, 110, 200, 30))
        self.lineEdit_mf2.setGeometry(QtCore.QRect(225, 110, 100, 30))
        
        self.label_mf3.setText("Smoothing") 
        self.lineEdit_mf3.setText("100") 
        self.label_mf3.setGeometry(QtCore.QRect(25, 150, 200, 30))
        self.lineEdit_mf3.setGeometry(QtCore.QRect(225, 150, 100, 30))
        
        self.pushButton_mf = QtWidgets.QPushButton(self.maxforceBox)
        self.pushButton_mf.setObjectName("pushButton_mf")
        self.pushButton_mf.setText("Calibrate Maxforce!")
        self.pushButton_mf.setGeometry(QtCore.QRect(190, 190, 200, 30))
        
        QtCore.QMetaObject.connectSlotsByName(Dialog1)



class Ui_Dialog2:
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.setGeometry(700,200,550,250)
        
        self.maxforceBox2 = QtWidgets.QMessageBox(Dialog2)
        self.maxforceBox2.setObjectName("maxforceBox2")
        self.maxforceBox2.setWindowTitle("Calculate Maxforce")
        self.maxforceBox2.setText("Continue in current log? y / n")
        self.maxforceBox2.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        self.res=self.maxforceBox2.exec_()
        QtCore.QMetaObject.connectSlotsByName(Dialog2)


class Ui_Dialog3:
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        left = 650
        top = 100
        width = 1008
        height = 720
        Dialog3.setGeometry(left, top, width, height)
        
        self.maxforceBox3 = QtWidgets.QWidget(Dialog3)
        self.maxforceBox3.setObjectName("maxforceBox3")
        self.maxforceBox3.setWindowTitle("Maxforce")
        
        QtCore.QMetaObject.connectSlotsByName(Dialog3)
        
        
class Ui_Dialog4:
    def setupUi(self, Dialog4):
        Dialog4.setObjectName("Dialog4")
        Dialog4.setGeometry(700,200,550,250)
        
        self.maxforceBox4 = QtWidgets.QMessageBox(Dialog4)
        self.maxforceBox4.setObjectName("maxforceBox4")
        self.maxforceBox4.setWindowTitle("Maxforce is calculated")
        self.maxforceBox4.setText("Current maxforce calculations are plotted and saved. If unsatisfactory, delete selected files and re-collect maxforce files")
        self.maxforceBox4.setStandardButtons(QtWidgets.QMessageBox.Ok)
        res=self.maxforceBox4.exec_()
        if res == QtWidgets.QMessageBox.Ok:
                print('\n_____________________\n \n CURRENT MAXFORCE CALCULATIONS ARE PLOTTED AND SAVED. IF UNSATISFACTORY, DELETE SELECTED FILES AND RE-COLLECT MAXFORCE FILES  \n_____________________\n')
                self.maxforceBox4.close()
        
        QtCore.QMetaObject.connectSlotsByName(Dialog4)
        
    


#%% 

class MaxforceDialog(QDialog):
    def __init__(self, parent=None):
        super(MaxforceDialog, self).__init__(parent)
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self)
        
        self.ui.pushButton_mf.clicked.connect(self.return_input)
        
    def return_input(self):
        self.test_duration = self.ui.lineEdit_mf1.text()
        self.scaling_size = self.ui.lineEdit_mf2.text()
        self.smoothing = self.ui.lineEdit_mf3.text()
        self.hide()
        
        return [self.test_duration, self.scaling_size, self.smoothing]
          


class MaxforceCalcDialog(QDialog):
    def __init__(self, parent=None):
        super(MaxforceCalcDialog, self).__init__(parent)

        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
         
        
    def run_it(self):
        import os 
        res = self.ui.res
        from psychopy import event
        keys=event.getKeys()
        if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
            print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %os.getcwd()) 
            run="this"
            
        if res == QtWidgets.QMessageBox.No or len(keys)>0 and keys[0] == 'n':
            print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %os.getcwd())
            run="new"
            
        if res == QtWidgets.QMessageBox.Cancel or len(keys)>0 and keys[0] == 'q':
            run="none"
            self.hide()
        return run 
    
    
class MaxforcePlot(QDialog):
    def __init__(self, parent=None):
        super(MaxforcePlot, self).__init__(parent)
        
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        
        m = PlotCanvas(self)
        m.move(0,0)
        
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self)
        #self.show()


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, dpi=100):
        import matplotlib
        matplotlib.use('Qt5Agg')
        import matplotlib.pyplot as plt
        self.fig, self.axs = plt.subplots(2)
        self.fig.set_size_inches(14, 10)
        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()  

    
    def plot(self):
        import numpy as np 
        import pickle       
        import os 
        #self.mfdir = os.path.join(self.logdir,'Maxforce')
        (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper)=pickle.load(open('maxforce.pkl', "rb"), encoding="latin1") 
        
        Q=upper*100
        styles=['-','--',':']
        colors=['r','y']
        LW=2
        lw=3
        
        self.axs[0].axhspan(0,MaxL, color='0.2', alpha=0.1)
        self.axs[0].plot(tL[0],rawL[0],label="Test 1",color=colors[1],linestyle=styles[0],linewidth=lw)
        self.axs[0].axhline(QL1[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[0])
        self.axs[0].plot(tL[1],rawL[1],label="Test 2",color=colors[1],linestyle=styles[1],linewidth=lw)
        self.axs[0].axhline(QL2[1], label=".%.f Upper Quantile"%Q,color='k', alpha=0.5,linewidth=LW,linestyle=styles[1])
        self.axs[0].plot(tL[2],rawL[2],label="Test 3",color=colors[1],linestyle=styles[2],linewidth=lw)
        self.axs[0].axhline(QL3[1], label=".%.f Upper Quantile"%Q,color='k', alpha=0.5,linewidth=LW,linestyle=styles[2])
        self.axs[0].axhline(MaxL, label="Maxforce", color=colors[1], alpha=0.5,linewidth=lw,linestyle=styles[0])
        self.axs[0].set_title('Left hand max force [%.f Newton]'%(MaxL))
        self.axs[0].legend(loc='lower right', ncol=4)
        self.axs[0].set_ylabel('[Newton]')
        
        self.axs[1].axhspan(0, MaxR, color='0.2', alpha=0.1)
        self.axs[1].plot(tR[0],rawR[0],label="Test 1",color=colors[0],linestyle=styles[0],linewidth=lw)
        self.axs[1].axhline(QR1[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[0])
        self.axs[1].plot(tR[1],rawR[1],label="Test 2",color=colors[0],linestyle=styles[1],linewidth=lw)
        self.axs[1].axhline(QR2[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[1])
        self.axs[1].plot(tR[2],rawR[2],label="Test 3",color=colors[0],linestyle=styles[2],linewidth=lw)
        self.axs[1].axhline(QR3[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[2])
        self.axs[1].axhline(MaxR, label="Maxforce", color=colors[0], alpha=0.5,linewidth=lw,linestyle=styles[0])
        self.axs[1].set_title('Right hand max force [%.f Newton]'%(MaxR)) 
        self.axs[1].legend(loc='lower right',ncol=4)
        self.axs[1].set_ylabel('[Newton]')
        
        self.axs[0].set_xlabel('Seconds')
        self.axs[1].set_xlabel('Seconds')
        
        maxT=max([max([max(i) for i in tL]),max([max(i) for i in tR])])
        self.axs[0].set_xlim(0,maxT) # min([min(i) for i in tL])-0.1, max([max(i) for i in tL])+0.1
        self.axs[1].set_xlim(0,maxT) # min([min(i) for i in tR])-0.1, max([max(i) for i in tR])+0.1
        self.axs[0].set_xticks(np.arange(0,maxT,1)) 
        self.axs[1].set_xticks(np.arange(0,maxT,1)) 
        
        #self.fig.set_size_inches(14, 10)
        self.fig.savefig('MaxForces.png', dpi=100)
        self.fig.tight_layout()
        
        self.draw()
        # import random 
        # data = [random.random() for i in range(250)]
        # ax = self.figure.add_subplot(111)
        # ax.plot(data, 'r-', linewidth = 0.5)
        # ax.set_title('PyQt Matplotlib Example')
        # self.draw()


    


     





#### Introduce def_settings widget here instead of in MainExperiment.py.  



#%%
class helpers:
    def __init__(self, parent=None):
        super(helpers, self).__init__(parent)
        
    def save_log(logno): 
        import os 
        import sys
        path = os.path.split(sys.argv[0])[0]
        
        import datetime, time 
        timestamp=time.time()
        timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d')
        print('\n_____________________\n \n LOG CREATED: %s %s \n_____________________\n' %(logno, timestamp_readable))    
     
        import os 
        if not os.path.exists('DATA'): os.makedirs('DATA')
        datapath=os.path.join(path,'DATA')
        
        log_ID = str(logno+'_'+timestamp_readable)
        
        os.chdir(datapath)
        if not os.path.exists(log_ID): os.makedirs(log_ID)
        logdir=os.path.join(datapath,log_ID)
        
        os.chdir(logdir)
        if not os.path.exists('Maxforce'): os.makedirs('Maxforce')
        print('\n_____________________\n \n FOLDERS CREATED: %s  \n_____________________\n' %logdir)
        os.chdir(path) 
        return logdir
        ############################
    
    def loop_maxforce(logdir, test_duration, scaling_size, smoothing):
        import os 
        import fnmatch 
        import MaxForceTest as MFT 
        from psychopy import event 
    
        L_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceL*'))
        R_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceR*'))
                        
        stoploop = False 
        keys=event.getKeys()
        while not stoploop:
            L_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceL*'))
            R_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceR*'))
            
            if L_reps<3 :  
                print('\n_____________________\n \n COLLECTING LEFT-HAND MAXFORCE FILES  \n_____________________\n')
                hand='L'
                MFT.run_maxforce(logdir, hand, test_duration, scaling_size, smoothing) 
        
            if R_reps<3 :  
                print('\n_____________________\n \n COLLECTING RIGHT-HAND MAXFORCE FILES  \n_____________________\n')
                hand='R'
                MFT.run_maxforce(logdir, hand, test_duration, scaling_size, smoothing) 
                
            if L_reps>=3 and R_reps>=3:
                print('\n_____________________\n \n MAXFORCE CALIBRATION FILES EXISTS IN FOLDER  \n_____________________\n')
                stoploop=True 
            
            # MANUALLY END EXPERIMENT
            keys=event.getKeys()
            if len(keys)>0:
                if keys[0] == 'q':
                    stoploop = True   
    
    
    def calc_max(logdir, run):  
        import os 
        import fnmatch
        import MaxForceCalc as MFCalc
        #from PyQt5 import QtGui
        #from PyQt5.QtGui import QPixmap, QIcon 
        import numpy as np
        import pickle
        
        if run == 'this':
            os.chdir(logdir)
            print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %os.getcwd()) 
            mfdir = os.path.join(logdir,'Maxforce')
            os.chdir(mfdir)
            
        if run == 'new':
            logdir = QtWidgets.QFileDialog.getExistingDirectory(None,'Select LOG Folder')
            os.chdir(logdir)
            print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %os.getcwd())
            mfdir = os.path.join(logdir,'Maxforce')
            os.chdir(mfdir)
            
         
        L_reps=len(fnmatch.filter(os.listdir(mfdir), 'maxforceL*'))
        R_reps=len(fnmatch.filter(os.listdir(mfdir), 'maxforceR*'))
        if L_reps<3 and R_reps<3:
            print('\n_____________________\n \n NOT ENOUGH MAXFORCE CALIBRATION FILES  \n_____________________\n')
            (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper) = [] 
            
        else:
            (maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper) = MFCalc.calc_maxforce(logdir, mfdir) # to save or not to save 
            save_it=np.array((maxforce, MaxL, MaxR, tL, rawL, tR, rawR, QL1, QL2, QL3, QR1, QR2, QR3, upper), dtype=object)
            pickle.dump(save_it,open(os.path.join(mfdir,'maxforce.pkl'),"wb"))

        os.chdir(os.path.dirname(os.path.dirname(logdir)))
        return maxforce



#%% 
# file main.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.pushButton1.clicked.connect(self.activate_tab_1)
        self.ui.pushButton2.clicked.connect(self.activate_tab_2)
        self.ui.pushButton3.clicked.connect(self.activate_tab_3)
        self.ui.pushButton4.clicked.connect(self.activate_tab_4)
        self.ui.pushButton5.clicked.connect(self.close)
        #import sys
        #self.ui.pushButton5.clicked.connect(sys.exit)
    

    def activate_tab_1(self):
        self.hide()
        self.loginput = self.ui.lineEdit.text()
        ############################
        logno = str(self.loginput)
        self.logdir = helpers.save_log(logno)
        ############################
        self.ui.label1.setText("Log is defined!")
        self.show()
        

    def activate_tab_2(self):
        self.hide()
        #####################
        mfd = MaxforceDialog(parent=self)
        mfd.exec()
        [self.test_duration, self.scaling_size, self.smoothing] = mfd.return_input()       
        helpers.loop_maxforce(self.logdir, int(self.test_duration), int(self.scaling_size), int(self.smoothing))  
        #####################
        self.ui.label2.setText("Maxforce files exists in folder!")
        self.show()
    

    def activate_tab_3(self):
        self.hide()
        ######################
        mfd2 = MaxforceCalcDialog(parent=self)
        run = mfd2.run_it()
        import os 
        import sys 
        if run != "none": 
            self.maxforce = helpers.calc_max(self.logdir, run)
            os.chdir(os.path.join(self.logdir,'Maxforce'))
            MaxforcePlot(parent=self)
            #####################
            self.ui.label3.setText("Maxforce is calculated!")
            os.chdir(os.path.split(sys.argv[0])[0])
        self.show()
    
    
    def activate_tab_4(self):
        self.hide()
        ######################
        import Settings as Settings
        self.settings = Settings.def_settings(self.logdir)
        print(type(self.settings))
        if type(self.settings) != 'str':
            import MainExperiment as MainExperiment
            MainExperiment.run_it(self.settings, self.logdir, self.maxforce)
            ######################
            self.ui.label4.setText("Experiment is done!")
        self.show()
        
        
    
    
    
    
    
#%% 

# if __name__ == '__main__':
#     # get path to script 
#     import os 
#     import sys
#     path = os.path.split(sys.argv[0])[0]
#     os.chdir(path)
    
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
    
#     sys.exit(app.exec_())
#     exit() 
    
    
    
    