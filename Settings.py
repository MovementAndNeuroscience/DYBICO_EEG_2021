# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:22:12 2021
@author: dzn332

DEFAULT SETTINGS
"""
## introducr timestamp på settings!! eller warning! 

##########################################################################
def def_settings(logdir):
    import sys
    import pandas as pd
    from PyQt5 import QtWidgets
    from psychopy import event
    QtWidgets.QApplication(sys.argv)
    msgBox = QtWidgets.QMessageBox(text="Load experimental settings from a file?")
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
    msgBox.addButton("Define new", QtWidgets.QMessageBox.AcceptRole)
    msgBox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
    res = msgBox.exec_()  
    keys=event.getKeys()
    
    if res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
        filedir = QtWidgets.QFileDialog.getOpenFileName(None,'Select file with experimental settings')
        settings = pd.read_pickle(filedir[0])
        
    if res == QtWidgets.QMessageBox.AcceptRole:
        import Settings as default_settings
        settings = default_settings.define_settings(logdir)
        
    if res == QtWidgets.QMessageBox.Cancel or len(keys)>0 and keys[0] == 'q':
        msgBox.hide()
        settings="none"
        
    return settings 


##########################################################################
# GUI for defining and saving experimental settings 
def define_settings(logdir):  
    from psychopy import gui, visual 
    mywin1 = visual.Window([512,512]) # create a window
    sets=gui.Dlg(title='DEFINE SETTINGS')
    sets.addText('Conditions to include: (baseline is always included)')
    sets.addField('Left-hand increase force',initial=True)
    sets.addField('Left-hand decrease force',initial=True)
    sets.addField('Right-hand increase force',initial=True)
    sets.addField('Right-hand decrease force',initial=True)
    sets.addField('Symmetrical increase force',initial=True)
    sets.addField('Symmetrical decrease force',initial=True)
    sets.addField('Left increase + Right decrease',initial=True)
    sets.addField('Left decrease + Right increase',initial=True)
    
    sets.addText('Define experimental settings:')
    sets.addField('Number of blocks: [1<]', 2)
    sets.addField('Time between blocks: [seconds]', 10)
    sets.addField('Trial repetitions within block:', 3)
    sets.addField('Trial duration: [seconds]', 2)
    sets.addField('Jitter time: [seconds]', 0.1)
    sets.addField('Baseline duration between trials: [seconds]', 2) 
    
    sets.addText('Visual feedback:')
    sets.addField('Percent change from baseline:',0.5)
    sets.addField('Percent of maxforce to reach baseline:',0.05)
    sets.addField('Sample smoothing:',100)
        
    sets.show()
    if gui.OK:
        import pandas as pd
        tasks = pd.DataFrame()
        tasks['Baseline_force'] = ['Y']
        if sets.data[0]==True: tasks['Left_increase_force'] = ['Y'] 
        elif sets.data[0]!=True: tasks['Left_increase_force'] = [''] 
        if sets.data[1]==True: tasks['Left_decrease_force'] = ['Y']
        elif sets.data[1]!=True: tasks['Left_decrease_force'] = ['']
        if sets.data[2]==True: tasks['Right_increase_force'] = ['Y']
        elif sets.data[2]!=True: tasks['Right_increase_force'] = ['']
        if sets.data[3]==True: tasks['Right_decrease_force'] = ['Y']
        elif sets.data[3]!=True: tasks['Right_decrease_force'] = ['']
        if sets.data[4]==True: tasks['Sym_increase_force'] = ['Y']
        elif sets.data[4]!=True: tasks['Sym_increase_force'] = ['']
        if sets.data[5]==True: tasks['Sym_decrease_force'] = ['Y']
        elif sets.data[5]!=True: tasks['Sym_decrease_force'] = ['']
        if sets.data[6]==True: tasks['Asym_L_increase_R_decrease'] = ['Y']
        elif sets.data[6]!=True: tasks['Asym_L_increase_R_decrease'] = ['']
        if sets.data[7]==True: tasks['Asym_L_decrease_R_increase'] = ['Y']
        elif sets.data[7]!=True: tasks['Asym_L_decrease_R_increase'] = ['']
        
        settings_ = pd.DataFrame()
        settings_= tasks
        settings_['no_of_blocks']=sets.data[8]
        settings_['time_between_blocks']=sets.data[9]
        settings_['trial_repetitions']=sets.data[10]
        settings_['trial_duration']=sets.data[11]
        settings_['jitter_time']=sets.data[12]
        settings_['baseline_between_trials']=sets.data[13]
        settings_['percent_change_from_baseline']=sets.data[14]
        settings_['percent_of_maxforce']=sets.data[15]
        settings_['smoothing']=sets.data[16]
        settings_.to_pickle(gui.fileSaveDlg(initFilePath=logdir, initFileName="__settings__.pkl"))
        
    else:
        print('user cancelled')
        settings_="Not defined"
    mywin1.close()
    
    return settings_




