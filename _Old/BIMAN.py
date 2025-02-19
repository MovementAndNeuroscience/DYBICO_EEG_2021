# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:11:58 2021
@author: Keenie Ayla

######## SCRIPT FOR RUNNING BIMANUAL EXERCISE ########

PROGRAM IS INITIATED BY CLICKING GREEN PLAY BUTTON
THE PROGRAM QUITS ON CLICKING "q"

If used in a new python installation, please go to the anaconda prompt and:
    pip install psychopy
    
    
try to remove dump. file saved if running from server. 

timing information, onsets, duration, trial order, 
log tidspunkt for win.flip()
"""

#%%

if __name__=='__main__':
    ######################
    import os
    path = os.getcwd()
    if path[-14:] != 'BIMANUAL_KAA21':
        import sys
        from PyQt5 import QtWidgets  
        QtWidgets.QApplication(sys.argv)
        path = QtWidgets.QFileDialog.getExistingDirectory(None,'Select BIMAN Folder')
        os.chdir(path)
    print('\n_____________________\n \n WORKING IN: %s  \n_____________________\n' %os.getcwd())
    

    #####################
    import Helpers as Helpers
    logdir = Helpers.logExp(path)
    
    ######################
    import MaxForceTest as MaxForceTest
    MaxForceTest.test_maxforce(logdir)
    
    ######################
    import MaxForceCalc as MaxForceCalc 
    %matplotlib qt
    maxforce = MaxForceCalc.calc_maxforce(logdir)
    
    ######################
    import MainExperiment as MainExperiment
    settings = MainExperiment.def_settings()
    MainExperiment.run_it(settings, logdir, maxforce)
    













   
    
   














   
    
   