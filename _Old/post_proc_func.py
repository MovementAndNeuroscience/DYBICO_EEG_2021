# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:46:55 2021

@author: dzn332
"""

def post_proc(filepath):
    import pandas as pd 
    file=pd.read_pickle(filepath)

    #%% Making a new dataframe easier to work with 
    trial_no = file['trial'][0] 
    trial_shifts = file['save_trialshift'][0] 
    
    data = pd.DataFrame()
    indices = []
    targets_, onsets_, durations_, t_ = [],[],[],[]
    for j in range(len(trial_shifts)): 
        targets_.append(str(trial_shifts[j][1]+str(trial_shifts[j][0])))
        [_, _, onset, duration, t]=trial_shifts[j] 
        onsets_.append(onset)
        durations_.append(duration)
        t_.append(t)
        # we need to seperate the data according to trial, so we group the indices 
        trial_ = trial_shifts[j][0]
        indices_ = [i for i, x in enumerate(trial_no) if x == trial_]
        indices.append(indices_)
    data['targetTrial'] = targets_
    data['onsets']= onsets_
    data['duration'] = durations_
    data['t'] = t_ 
    data['indices'] = indices 
    
    
    
    
    #%% We drop all intermediate data from this new dataframe 
    dropindex = []
    for j in range(len(trial_shifts)): 
        dropindex.append(data['targetTrial'][j][:5] =='Pause')
        if dropindex[j] == False : dropindex[j] = data['duration'][j]==0.5000 
    data['dropindex']=dropindex
    
    
    #%% 
    import numpy as np
    force_L, force_R, time, fliptime, target_names, targets = [], [], [],[], [],[]
    test_unique = []
    for j in range(len(trial_shifts)):
        idx = data.loc[j,'indices']
        force_L.append(file['left_force'][0][min(idx):max(idx)+1])
        force_R.append(file['right_force'][0][min(idx):max(idx)+1])
        time.append(file['time'][0][min(idx):max(idx)+1])
        fliptime.append(file['fliptime'][0][min(idx):max(idx)+1])
        target_names.append(file['target_name'][0][min(idx):max(idx)+1])
        targets.append(file['target'][0][min(idx):max(idx)+1])
        test_unique.append(np.unique(file['target_name'][0][min(idx):max(idx)+1]))
        
    data['force_L'] = force_L
    data['force_R'] = force_R
    data['time'] = time
    data['fliptime'] = fliptime
    data['targets'] = targets
    data['target_names'] = target_names

    
    #%% Save the data file 
    import os
    import datetime, time 
    timestamp=time.time()
    timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H%M')
    save_in = os.path.split(filepath)[0]
    save_it_as_pkl = os.path.join(save_in,str("DATA_file_"+timestamp_readable+".pkl"))
    data.to_pickle(save_it_as_pkl)
    
    
    
    



