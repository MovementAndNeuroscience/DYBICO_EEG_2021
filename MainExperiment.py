# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:24:50 2021
@author: Keenie Ayla
MAIN EXPERIMENT


"""

##########################################################################
def run_it(settings, logdir, maxforce):
    import Helpers as kaah # helper functions import 
    
    
    ##########################################################################
    # file for saving 
    import os
    import pandas as pd 
    import datetime, time 
    timestamp=time.time()
    timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H%M')
    save_it = pd.DataFrame()
    save_it_as_pkl = os.path.join(logdir,str("output_file_"+timestamp_readable+".pkl"))
    #save_it_as_csv = str(logdir+"\output_file2_"+timestamp_readable+".csv")


    ##########################################################################
    import numpy as np
    path = os.getcwd() 
    print('\n_____________________\n \n RUNNING IN: %s  \n_____________________\n' %logdir)
    
    tasks = settings[['Baseline_force', 'Left_increase_force', 'Left_decrease_force', 'Right_increase_force', 'Right_decrease_force', 'Sym_increase_force', 'Sym_decrease_force', 'Asym_L_increase_R_decrease', 'Asym_L_decrease_R_increase']]
    sets_= np.array(settings[['percent_of_maxforce', 'percent_change_from_baseline', 'trial_duration', 'jitter_time', 'baseline_between_trials', 'trial_repetitions', 'no_of_blocks', 'time_between_blocks', 'smoothing']]).flatten()
    [percent_of_maxforce, percent_change_from_baseline, trial_duration, jitter_time,  baseline_between_trials, trial_repetitions, no_of_blocks, time_between_blocks, smoothing]=sets_
    no_of_blocks=int(no_of_blocks)
    trial_repetitions=int(trial_repetitions)    
    smoothing=int(smoothing)
    
    
    ##########################################################################
    # # DEFINE CIRCLE GOAL/TARGET SIZES - DEPENDING ON CONDITIONS SELECTED    
    LH = RH = 0.5 # baseline relative size of circle
    inter_target = (LH, RH) # size of intermediate baseline
    pause_target = (0.01,0.01) # size of pause between blocks
    (targets, targets_names) = kaah.get_targets(tasks, LH, RH, percent_change_from_baseline, pause_target)
    
    
    ##########################################################################
    # DEFINE ONSETS AND DURATIONS IN BLOCK STRUCTURE
    initial_dur = 0.5 # duration of baseline before experiment start
    (conditions, durations, onsets) = kaah.get_block(no_of_blocks, trial_repetitions, targets, jitter_time, trial_duration, baseline_between_trials, initial_dur, time_between_blocks)
    baseline_onsets = onsets+durations 
    #print(baseline_onsets)
    
    ##########################################################################
    # open inititation GUI interface 
    import sys
    from PyQt5 import QtWidgets
    from psychopy import event
    QtWidgets.QApplication(sys.argv)
    msgBox2 = QtWidgets.QMessageBox(text="READY TO INITIATE EXPERIMENT?")
    msgBox2.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
    res = msgBox2.exec_()  
    keys=event.getKeys()
    if res == QtWidgets.QMessageBox.Cancel:
        msgBox2.hide()
    elif res == QtWidgets.QMessageBox.Yes or len(keys)>0 and keys[0] == 'y':
        print(' ')
    log_ID = os.path.split(logdir)[1] #logdir[(len(str(os.path.join(path,'DATA')))):]
    
    
    ##########################################################################
    # variables for saving
    save_it['log'] = [logdir]
    #save_it['maxforceLR'] = ['']
    save_it['maxforceLR'] = [maxforce] 
    save_it['settings']=[settings] 
    save_it['set_conditions']=[conditions]
    save_it['set_durations']=[durations]
    save_it['set_onsets']=[onsets]
    
    save_forceL = []
    save_forceR = []
    save_time = []
    save_fliptime = []
    save_targetname = []
    save_target_ = []
    save_trialshift = []
    save_trial = []
    ## igen drop append 
    
    
    ##########################################################################
    # DEFINE EXP WINDOW
    from psychopy import visual 
    mywin=visual.Window(size=[1000,1000],fullscr=False,screen=0) # changed from 800, 600
    mywin.setMouseVisible(True)
    scene=kaah.CircleScene(mywin)
    
    
    ##########################################################################
    # SAVE DATA UNDER LOG_ID
    import datetime, time 
    timestamp=time.time()
    timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H-%M-%S')
    filename=log_ID+'_%s.raw'%timestamp_readable
    
    
    ##########################################################################
    # READ FROM APPLEJACK DEVICE AND CORRECT OFFSET
    import aReader_KAA as aReader 
    import os 
    os.chdir(logdir)
    appleJack=aReader.aReader(debug=False,dump=filename)
    offset = np.array((1575,1575))[None]    
    #calipath = os.path.join(os.path.dirname(os.path.dirname(logdir)),'Calibration','calicoefs.npy')
    #[Lcoef, Lint, Rcoef, Rint]=np.load(calipath)    


    ##########################################################################
    # Triggers to EEG system 
    send_trigger = False
    trigger_state = 0
    
    
    ##########################################################################
    # LIVE READING OF DEVICE INPUT 
    stop = False
    from psychopy import core, event
    trial = 0
    baseline_break = 0
    globalClock = core.Clock()
    t0 = globalClock.getTime()
    global_time = time.time()
    
    while not stop:
        send_trigger = False
        t = globalClock.getTime()-t0
        save_time.append(t)
        if trial<len(onsets)-1 and t>=onsets[trial+1]:
            trial += 1
            print('Trial %s of %s - ' %(trial, len(onsets)-1) +targets_names[conditions[trial]])
            save_trialshift.append([trial, targets_names[conditions[trial]], onsets[trial], durations[trial], t])
            
            kaah.trigger(trigger_state=conditions[trial], send_trigger=True)
            send_trigger = False
            
        if baseline_break<len(baseline_onsets)-1 and t>=1 and t>=baseline_onsets[baseline_break+1]:
            baseline_break += 1
            print('Trial Back-to-baseline %s' %baseline_break)
            kaah.trigger(trigger_state=255, send_trigger=True)
            send_trigger = False
            
        if trial<len(onsets) and t-onsets[trial]<durations[trial]:
            scene.targetLeft,scene.targetRight = targets[conditions[trial]]
            save_targetname.append(targets_names[conditions[trial]])
            save_target_.append(targets[conditions[trial]])
            
        elif t>(onsets[-1]+durations[-1]):
            scene.targetLeft, scene.targetRight = pause_target
            save_targetname.append(targets_names[conditions[trial]])
            save_target_.append(pause_target)
            if t>(onsets[-1]+durations[-1]+2): # stop experiment after 2 sec 
                stop=True 
        else:
            scene.targetLeft, scene.targetRight = inter_target
            save_targetname.append(targets_names[conditions[trial]])
            save_target_.append(inter_target)

        save_trial.append(trial)
        
    ##########################################################################
    # READ INPUT WITH SPECIFIED SMOOTHING + SET MAXFORCE
        [maxL, maxR] = maxforce 
        v0=appleJack.getValues(smoothing)[:,1:]-offset 
        #v0_mean=v0.mean(0) # newton calibration
        #save_v0.append(v0_mean) # newton calibration
        #v = Rint + Rcoef*v0  # newton calibration
        v_mean=v0.mean(0)
        #save_v_mean.append(v_mean)
    
        scalingL=percent_of_maxforce*2
        scalingR=percent_of_maxforce*2
        # Scaling of the input is done, to ensure the input matches the target
        # circle range of 0-1. Thus the signal of each hand is divided by a
        # the maximum force of the corresponding hand. By doing so, the baseline 
        # target of 0.5, corresponds to half the maximum force. 
        # The needed force can then be further adjusted by introducing a 
        # scaling factor, which is defined as 2*the percent of maxforce that 
        # should match the baseline target. E.g. if baseline target should be 
        # 10% of maxforce, then scaling=0.1*2=0.2. If maxforce=200 then the 
        # baseline target of 0.5, can be reached by providing input: 
        # circle_size = input/(max*(2*percent_max)) 
        # circle_size*(max*(2*percent_max)) = input 
        # 0.5*(200*(2*0.1)) = input ==> input = 20 
        # Thus the input required to match baseline is 20, which compared to
        # maxforce of 200, is 10%
        
        scene.left = v_mean[1]/(maxL*scalingL)
        scene.right = v_mean[0]/(maxR*scalingR)
        save_forceL.append(v_mean[1]/(maxL*scalingL))
        save_forceR.append(v_mean[0]/(maxR*scalingR))
       
    ##########################################################################
    # CALL CircleScene Class DEFINITION TO DRAW
        scene.draw()
        mywin.flip()    
        save_fliptime.append(globalClock.getTime()-t0)    
    # SEND TRIGGER 
    #trigger(trigger_state, send_trigger, trigger_time, )
        
        
    #########################################################################
    # MANUALLY END EXPERIMENT
        keys=event.getKeys()
        if len(keys)>0:
            if keys[0] == 'q':
                stop = True
                os.chdir(path)
                print('\n_____________________\n \n EXPERIMENT CANCELLED BY USER  \n_____________________\n')


    save_it['GlobalTime']=[global_time]
    save_it['target_name'] = [save_targetname]
    save_it['target'] = [save_target_]
    save_it['trial'] = [save_trial]
    save_it['left_force'] = [save_forceL]
    save_it['right_force'] = [save_forceR]
    save_it['time'] = [save_time]
    save_it['fliptime'] = [save_fliptime]
    save_it['save_trialshift']=[save_trialshift]
    
    save_it.to_pickle(save_it_as_pkl)
    print('\n_____________________\n \n DATA SAVED IN : %s  \n_____________________\n' %logdir)
    appleJack.stop()
    del appleJack
    mywin.close()
    #core.quit()
    os.chdir(path)
    
    #%% Making another dataframe 
    #kaah.reshape_data(save_it_as_pkl)



#%% 



