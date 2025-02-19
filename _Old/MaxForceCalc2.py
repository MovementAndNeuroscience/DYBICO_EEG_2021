# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:37:51 2021

@author: dzn332
"""
# import sys

# from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
# from PyQt5.QtGui import QIcon


# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt


def myfunc(logdir, mfdir):
    from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
    from PyQt5.QtGui import QIcon
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure   
    import sys 
    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import Helpers as helpers 
    import os 
    os.chdir(mfdir)
    
    (L1, tL1, L2, tL2, L3, tL3, R1, tR1, R2, tR2, R3, tR3) = helpers.load_maxes()

    # all values below 10 [native units] are 0grams, so we exclude dem from the calculations
    lim=10 ### 
    rawL=[np.array(L1[L1>lim]), np.array(L2[L2>lim]), np.array(L3[L3>lim])]
    rawR=[np.array(R1[R1>lim]), np.array(R2[R2>lim]), np.array(R3[R3>lim])]
    
    # we adjust the time, to only look at the task ON period
    tL=[np.array(tL1[L1>lim])-min(tL1), np.array(tL2[L2>lim])-min(tL2), np.array(tL3[L3>lim])-min(tL3)]
    tR=[np.array(tR1[R1>lim])-min(tR1), np.array(tR2[R2>lim])-min(tR2), np.array(tR3[R3>lim])-min(tR3)]
    
    # calculate 75th percentile 
    upper = 0.75
    (QL1,QL2,QL3,QR1,QR2,QR3,MaxL,MaxR,maxforce) = helpers.calc_perc_raw(rawL,rawR,upper)
    
    #################### INTRODUCING NEWTON #########################
    calipath = os.path.join(os.path.dirname(os.path.dirname(logdir)),'Calibration','calicoefs.npy')
    [Lcoef, Lint, Rcoef, Rint]=np.load(calipath) 
    rawL=[Lint + Lcoef*np.array(L1[L1>lim]), Lint + Lcoef*np.array(L2[L2>lim]), Lint + Lcoef*np.array(L3[L3>lim])]
    rawR=[Rint + Rcoef*np.array(R1[R1>lim]), Rint + Rcoef*np.array(R2[R2>lim]), Rint + Rcoef*np.array(R3[R3>lim])]
    (QL1,QL2,QL3,QR1,QR2,QR3,MaxL,MaxR,_) = helpers.calc_perc_raw(rawL,rawR,upper)
        
        
    class App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.left = 650
            self.top = 100
            self.title = 'Maxforce'
            self.width = 1008
            self.height = 720
            self.initUI()
    
        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            m = PlotCanvas(self)
            m.move(0,0)
            self.show()
    
    class PlotCanvas(FigureCanvas):
        def __init__(self, parent=None, dpi=100): # width=5, height=4,
            #fig = Figure(figsize=(width, height), dpi=dpi)
            #self.axes = fig.add_subplot(111)
            self.fig, self.axs = plt.subplots(2)
            self.fig.set_size_inches(14, 10)
            
            FigureCanvas.__init__(self, self.fig)
            self.setParent(parent)
            FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
            FigureCanvas.updateGeometry(self)
            self.plot()        

        def plot(self):
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
    
            
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
     

logdir="C:/Users/dzn332/Documents/D-BICO/DATA/test_20211202"
mfdir="C:/Users/dzn332/Documents/D-BICO/DATA/test_20211202/Maxforce"
myfunc(logdir, mfdir)

#%%




##########################################################################
# plotting maxforce 
def plot_maxforce(logdir, mfdir):
    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import os 
    
    # loading the data only for the task ON period 
    ONidx= [i for i, e in enumerate((pd.read_pickle('.\\maxforceL1')['TrialType'][0])) if e == 1]    
    L1=np.array(pd.read_pickle('.\\maxforceL1')['Left'][0][ONidx[0]:ONidx[-1]])
    tL1=np.array(pd.read_pickle('.\\maxforceL1')['Fliptime'][0][ONidx[0]:ONidx[-1]])
    
    ONidx= [i for i, e in enumerate((pd.read_pickle('.\\maxforceL2')['TrialType'][0])) if e == 1]    
    L2=np.array(pd.read_pickle('.\\maxforceL2')['Left'][0][ONidx[0]:ONidx[-1]])
    tL2=np.array(pd.read_pickle('.\\maxforceL2')['Fliptime'][0][ONidx[0]:ONidx[-1]])

    ONidx= [i for i, e in enumerate((pd.read_pickle('.\\maxforceL3')['TrialType'][0])) if e == 1]    
    L3=np.array(pd.read_pickle('.\\maxforceL3')['Left'][0][ONidx[0]:ONidx[-1]])
    tL3=np.array(pd.read_pickle('.\\maxforceL3')['Fliptime'][0][ONidx[0]:ONidx[-1]])
    
    ONidx= [i for i, e in enumerate((pd.read_pickle('.\\maxforceR1')['TrialType'][0])) if e == 1]    
    R1=np.array(pd.read_pickle('.\\maxforceR1')['Right'][0][ONidx[0]:ONidx[-1]])
    tR1=np.array(pd.read_pickle('.\\maxforceR1')['Fliptime'][0][ONidx[0]:ONidx[-1]])

    ONidx= [i for i, e in enumerate((pd.read_pickle('.\\maxforceR2')['TrialType'][0])) if e == 1]    
    R2=np.array(pd.read_pickle('.\\maxforceR2')['Right'][0][ONidx[0]:ONidx[-1]])
    tR2=np.array(pd.read_pickle('.\\maxforceR2')['Fliptime'][0][ONidx[0]:ONidx[-1]])

    ONidx= [i for i, e in enumerate((pd.read_pickle('.\\maxforceR3')['TrialType'][0])) if e == 1]        
    R3=np.array(pd.read_pickle('.\\maxforceR3')['Right'][0][ONidx[0]:ONidx[-1]])
    tR3=np.array(pd.read_pickle('.\\maxforceR3')['Fliptime'][0][ONidx[0]:ONidx[-1]])
    

    # all values below 10 [native units] are 0grams, so we exclude dem from the calculations
    lim=10 ### 
    rawL=[np.array(L1[L1>lim]), np.array(L2[L2>lim]), np.array(L3[L3>lim])]
    rawR=[np.array(R1[R1>lim]), np.array(R2[R2>lim]), np.array(R3[R3>lim])]
    
    # we adjust the time, to only look at the task ON period
    tL=[np.array(tL1[L1>lim])-min(tL1), np.array(tL2[L2>lim])-min(tL2), np.array(tL3[L3>lim])-min(tL3)]
    tR=[np.array(tR1[R1>lim])-min(tR1), np.array(tR2[R2>lim])-min(tR2), np.array(tR3[R3>lim])-min(tR3)]
    
    # calculate 75th percentile 
    upper = 0.75
    QL1=np.quantile(rawL[0], [0.5, upper])
    QL2=np.quantile(rawL[1], [0.5, upper])
    QL3=np.quantile(rawL[2], [0.5, upper])
    QR1=np.quantile(rawR[0], [0.5, upper])
    QR2=np.quantile(rawR[1], [0.5, upper])
    QR3=np.quantile(rawR[2], [0.5, upper])
    MaxL=np.mean([QL1[1],QL2[1],QL3[1]])
    MaxR=np.mean([QR1[1],QR2[1],QR3[1]])
    maxforce=[MaxL, MaxR] # NOT IN NETWON
    
    
    #################### INTRODUCING NEWTON #########################
    calipath = os.path.join(os.path.dirname(os.path.dirname(logdir)),'Calibration','calicoefs.npy')
    [Lcoef, Lint, Rcoef, Rint]=np.load(calipath) 
    
    rawL=[Lint + Lcoef*np.array(L1[L1>lim]), Lint + Lcoef*np.array(L2[L2>lim]), Lint + Lcoef*np.array(L3[L3>lim])]
    rawR=[Rint + Rcoef*np.array(R1[R1>lim]), Rint + Rcoef*np.array(R2[R2>lim]), Rint + Rcoef*np.array(R3[R3>lim])]
    QL1=np.quantile(rawL[0], [0.5, upper])
    QL2=np.quantile(rawL[1], [0.5, upper])
    QL3=np.quantile(rawL[2], [0.5, upper])
    QR1=np.quantile(rawR[0], [0.5, upper])
    QR2=np.quantile(rawR[1], [0.5, upper])
    QR3=np.quantile(rawR[2], [0.5, upper])
    MaxL=np.mean([QL1[1],QL2[1],QL3[1]])
    MaxR=np.mean([QR1[1],QR2[1],QR3[1]])
    
    
    ######################### PLOTTING ##############################
    Q=upper*100
    styles=['-','--',':']
    colors=['r','y']
    LW=2
    lw=3
    #%matplotlib qt
    fig, axs = plt.subplots(2)
    axs[0].axhspan(0,MaxL, color='0.2', alpha=0.1)
    axs[0].plot(tL[0],rawL[0],label="Test 1",color=colors[1],linestyle=styles[0],linewidth=lw)
    axs[0].axhline(QL1[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[0])
    axs[0].plot(tL[1],rawL[1],label="Test 2",color=colors[1],linestyle=styles[1],linewidth=lw)
    axs[0].axhline(QL2[1], label=".%.f Upper Quantile"%Q,color='k', alpha=0.5,linewidth=LW,linestyle=styles[1])
    axs[0].plot(tL[2],rawL[2],label="Test 3",color=colors[1],linestyle=styles[2],linewidth=lw)
    axs[0].axhline(QL3[1], label=".%.f Upper Quantile"%Q,color='k', alpha=0.5,linewidth=LW,linestyle=styles[2])
    axs[0].axhline(MaxL, label="Maxforce", color=colors[1], alpha=0.5,linewidth=lw,linestyle=styles[0])
    axs[0].set_title('Left hand max force [%.f Newton]'%(MaxL))
    axs[0].legend(loc='lower right', ncol=4)
    axs[0].set_ylabel('[Newton]')
    
    axs[1].axhspan(0, MaxR, color='0.2', alpha=0.1)
    axs[1].plot(tR[0],rawR[0],label="Test 1",color=colors[0],linestyle=styles[0],linewidth=lw)
    axs[1].axhline(QR1[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[0])
    axs[1].plot(tR[1],rawR[1],label="Test 2",color=colors[0],linestyle=styles[1],linewidth=lw)
    axs[1].axhline(QR2[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[1])
    axs[1].plot(tR[2],rawR[2],label="Test 3",color=colors[0],linestyle=styles[2],linewidth=lw)
    axs[1].axhline(QR3[1], label=".%.f Upper Quantile"%Q, color='k', alpha=0.5,linewidth=LW,linestyle=styles[2])
    axs[1].axhline(MaxR, label="Maxforce", color=colors[0], alpha=0.5,linewidth=lw,linestyle=styles[0])
    axs[1].set_title('Right hand max force [%.f Newton]'%(MaxR)) 
    axs[1].legend(loc='lower right',ncol=4)
    axs[1].set_ylabel('[Newton]')
    
    axs[0].set_xlabel('Seconds')
    axs[1].set_xlabel('Seconds')
    
    maxT=max([max([max(i) for i in tL]),max([max(i) for i in tR])])
    axs[0].set_xlim(0,maxT) # min([min(i) for i in tL])-0.1, max([max(i) for i in tL])+0.1
    axs[1].set_xlim(0,maxT) # min([min(i) for i in tR])-0.1, max([max(i) for i in tR])+0.1
    axs[0].set_xticks(np.arange(0,maxT,1)) 
    axs[1].set_xticks(np.arange(0,maxT,1)) 
    
    
    fig.set_size_inches(14, 10)
    fig.savefig('MaxForces.png', dpi=100)
    fig.tight_layout()
    #fig.show()
    #mngr = plt.get_current_fig_manager()
    # to put it into the upper left corner for example:
    #mngr.window.setGeometry(50,100,800, 545)
    
    # def show_max():
    #     from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    #     from matplotlib.figure import Figure
        
    
    
    
    # def show_max(mfdir):
    #     from PyQt5 import QtWidgets 
    #     from PyQt5.QtGui import QPixmap, QIcon 
    #     os.chdir(mfdir)
    #     icon = QIcon('MaxForces.png')
    #     imgbox = QtWidgets.QMessageBox()
    #     imgbox.setIconPixmap(icon.pixmap(1000, 1000))
    #     imgbox.show()
    #     return imgbox.exec_()
    # show_max(mfdir)
    
    return maxforce  # NOT IN NEWTON



##########################################################################






