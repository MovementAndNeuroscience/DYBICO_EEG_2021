# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:16:41 2021
@author: Keenie Ayla
MAXFORCE CALIBRATION FUNCTIONS 
"""

##########################################################################
# run 1 maxforce test and ask whether to save
def run_maxforce(logdir, hand, trial_duration, scaling_size, smoothing): 
    import os 
    mfdir=os.path.join(logdir,'Maxforce')
    path=os.path.dirname(os.path.dirname(logdir))
    os.chdir(path)
    
    #smoothing=10 # 100 before 
    if hand=='R': targets=['Right_max']
    if hand=='L': targets=['Left_max']
    
    durations=(trial_duration,)
    onsets=(3,) 
    
    from psychopy import visual
    mywin = visual.Window([800, 800])
    
    import numpy as np    
    p1=np.linspace(-.5*np.pi,.5*np.pi,256)
    halfc1=np.vstack((np.cos(p1),np.sin(p1))).T
    halfc2=np.vstack((-np.cos(p1),np.sin(p1))).T
    interp=True
    linewidth=5
    circ1= visual.ShapeStim(win=mywin, units='norm', lineWidth=linewidth, lineColor='red', lineColorSpace='rgb', fillColor=None,\
            fillColorSpace='rgb', vertices=halfc1, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
            interpolate=interp)
    circ2= visual.ShapeStim(win=mywin, units='norm', lineWidth=linewidth, lineColor='yellow', lineColorSpace='rgb', fillColor=None,\
            fillColorSpace='rgb', vertices=halfc2, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
            interpolate=interp)
    txt=visual.TextStim(mywin,pos=(0,.9))
    
    # READ FROM APPLEJACK DEVICE AND CORRECT OFFSET
    import aReader_KAA as aReader 
    pico=aReader.aReader(debug=False,dump='maxforce.raw')
    offset = np.array((1575,1575))[None]
    # introduce calibration, to Newton
    #calipath = os.path.join(os.path.dirname(os.path.dirname(logdir)),'Calibration','calicoefs.npy')
    #[Lcoef, Lint, Rcoef, Rint]=np.load(calipath)  

    # # LIVE READING OF DEVICE INPUT 
    stop = False
    from psychopy import core, event 
    import time 
    trial = 0
    trialtype=0 #'None'
    globalClock = core.Clock()
    t0 = globalClock.getTime()
    global_time = time.time()
    v_type, v_left, v_right, t_save, t_flip = [], [], [], [], []
    while not stop:
        t = globalClock.getTime()-t0
        v0=pico.getValues(smoothing)[:,1:]-offset
        #v0_mean=v0.mean(0) # introduce calibration, to Newton
        #v = Rint + Rcoef*v0 # introduce calibration, to Newton
        v=v0.mean(0)
        
        t_save.append(t)
        v_left.append(v[1])
        v_right.append(v[0])
        
        # global_time.append(time.time())
        # lav v_ lange lister, sæt værdier nok til 1.5 time, sampling rate 500hz, 
        # screen udpdate 60 i sec, 
        # men der er også en betydning med smoothing, 100 svarer til 100ms delay, 
        # 10 msec delay på device i sig selv, men det er irrelevant, så vores 
        # smoothing kommer oveni. 
        # evt. gem timestamp på maxforce tests, så at man kan genskabe rækkefølgen
        # omddøb i stedet for slet filer, for at gemme fejl 
        
        if t<onsets[trial] :
             if targets[trial] == 'Left_max': 
                 txt.setText('VENSTRE \n ')
                 txt.draw()
             if targets[trial] == 'Right_max':
                 txt.setText('HØJRE \n ')
                 txt.draw()
        if (onsets[trial])>t>(onsets[trial]-1) :
             if targets[trial] == 'Left_max': 
                 txt.setText('VENSTRE \n --- 1 ---')
             if targets[trial] == 'Right_max': 
                 txt.setText('HØJRE \n --- 1 ---')
        if (onsets[trial]-1)>t>(onsets[trial]-2) :
             if targets[trial] == 'Left_max': 
                 txt.setText('VENSTRE \n --- 2 ---')
             if targets[trial] == 'Right_max': 
                 txt.setText('HØJRE \n --- 2 ---')   
        if (onsets[trial]-2)>t>(onsets[trial]-3) :
             if targets[trial] == 'Left_max': 
                 txt.setText('VENSTRE \n --- 3 ---')
             if targets[trial] == 'Right_max': 
                 txt.setText('HØJRE \n --- 3 ---')
        txt.draw()
        
        if t>onsets[trial] and t-onsets[trial]<durations[trial]:   # trial<len(onsets)  
            if targets[trial] == 'Left_max':
                txt.setText('VENSTRE \n(%i)'%(v[1]))
                txt.draw()
                circ2.setSize(v[1]/scaling_size*np.array([1,1]))
                circ2.draw()
                trialtype=1
                
            if targets[trial] == 'Right_max':
                txt.setText('HØJRE \n(%i)'%(v[0]))
                txt.draw()
                circ1.setSize(v[0]/scaling_size*np.array([1,1]))
                circ1.draw()
                trialtype=1
            #v_type.append(trialtype)
        
        elif t>(onsets[-1]+durations[-1]+1): # stop after +1 sec 
                stop=True 
        
        
        mywin.flip()
        t_flip.append(globalClock.getTime()-t0)
        v_type.append(trialtype)
        
        # MANUALLY END EXPERIMENT
        keys=event.getKeys()
        if len(keys)>0:
            if keys[0] == 'q':
                stop = True
                
    pico.stop()
    del pico
    mywin.close()
    # core.quit()
    
    ##########################################################################
    # Make dataframe 
    import pandas as pd 
    maxforces = pd.DataFrame()
    maxforces['GlobalTime']=[global_time]
    maxforces['Left']=[v_left]
    maxforces['Right']=[v_right] 
    #maxforces['Raw']=[v0_mean]
    maxforces['TrialType']=[v_type]
    maxforces['Time']=[t_save]
    maxforces['Fliptime']=[t_flip] 
    

    
    ##########################################################################
    # to save or not to save 
    import sys
    from PyQt5 import QtWidgets
    from psychopy import event
    QtWidgets.QApplication(sys.argv)
    msgBox = QtWidgets.QMessageBox(text="Would you like to save the test?")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Abort)
    
    res = msgBox.exec_()  
    keys=event.getKeys()
    if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
        save=True 
    if res == QtWidgets.QMessageBox.No or len(keys)>0 and keys[0] == 'n':
        save=False
    if res == QtWidgets.QMessageBox.Abort :
        sys.exit()
    
    ########################################################################## 
    # save as...
    import fnmatch 
    if hand=='R': 
        if len(fnmatch.filter(os.listdir(mfdir), 'maxforceR1'))<1: saveno='1'
        elif len(fnmatch.filter(os.listdir(mfdir), 'maxforceR2'))<1: saveno='2' 
        elif len(fnmatch.filter(os.listdir(mfdir), 'maxforceR3'))<1: saveno='3'   
        else: saveno='_'
        savename='maxforceR'+saveno
        
    if hand=='L': 
        if len(fnmatch.filter(os.listdir(mfdir), 'maxforceL1'))<1: saveno='1'
        elif len(fnmatch.filter(os.listdir(mfdir), 'maxforceL2'))<1: saveno='2' 
        elif len(fnmatch.filter(os.listdir(mfdir), 'maxforceL3'))<1: saveno='3'   
        else: saveno='_'
        savename='maxforceL'+saveno    
        
    if save==True :
        maxforces.to_pickle(mfdir+str("/")+savename) 
        print('\n_____________________\n \n SAVED %s  \n_____________________\n' %savename)
    
    
    ##########################################################################
    # Continue or not continue   
    L_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceL*'))
    R_reps=len(fnmatch.filter(os.listdir(os.path.join(logdir,'Maxforce')), 'maxforceR*'))
    if L_reps>=3 and R_reps>=3: 
        QtWidgets.QApplication(sys.argv)
        msgBox2 = QtWidgets.QMessageBox(text="All maxforce calibration files have been acquired!")
        msgBox2.exec_()
    else : 
        QtWidgets.QApplication(sys.argv)
        if hand=='R': msgBox2 = QtWidgets.QMessageBox(text="Ready to collect another?")
        if hand=='L': msgBox2 = QtWidgets.QMessageBox(text="Ready to collect another?")
        #msgBox2 = QtWidgets.QMessageBox(text="Ready to collect another?")
        msgBox2.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Abort)
        res = msgBox2.exec_()  
        keys=event.getKeys()
        if res == QtWidgets.QMessageBox.Abort:
            sys.exit()
        elif res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
            print(' ')
    

    




















