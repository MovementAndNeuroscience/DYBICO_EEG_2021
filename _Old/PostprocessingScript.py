# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:57:03 2021
@author: dzn332

file for working with output files of .pkl format. 

"""

#%% Specify file 

filepath = 'C:/Users/dzn332/Documents/D-BICO/DATA/P001/DATA_file_20211123_1149.pkl'




#%% Read the file 
import pandas as pd 
file=pd.read_pickle(filepath)
file.keys() # to see what information is in the file 
# Out[11]: Index(['log', 'maxforceLR', 'conditions', 'settings'], dtype='object')
# settings = file['settings'][0]



#%% Making a new dataframe easier to work with 
trial_no = file['trial'][0] 
trial_shifts = file['save_trialshift'][0] # [trial, targets_names[conditions[trial]], onsets[trial], durations[trial], globalClock.getTime()-t0, t]

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
#data.drop(data[data['dropindex']==True].index, inplace=True )
#data.drop("dropindex",1,inplace=True)



#%% 
import numpy as np
force_L, force_R, v_mean, time, fliptime, target_names, targets = [],[], [], [],[], [],[]
test_unique = []
for j in range(len(trial_shifts)):
    idx = data.loc[j,'indices']
    force_L.append(file['left_force'][0][min(idx):max(idx)+1])
    force_R.append(file['right_force'][0][min(idx):max(idx)+1])
    #v.append(file['appleJack_raw'][0][min(idx):max(idx)+1])
    #v_mean.append(file['appleJack_smoothed'][0][min(idx):max(idx)+1])
    time.append(file['time'][0][min(idx):max(idx)+1])
    fliptime.append(file['fliptime'][0][min(idx):max(idx)+1])
    target_names.append(file['target_name'][0][min(idx):max(idx)+1])
    targets.append(file['target'][0][min(idx):max(idx)+1])
    test_unique.append(np.unique(file['target_name'][0][min(idx):max(idx)+1]))
    
data['force_L'] = force_L
data['force_R'] = force_R
#data['appleJack_raw'] = v
#data['appleJack_smoothed'] = v_mean
data['time'] = time
data['fliptime'] = fliptime
data['targets'] = targets
data['target_names'] = target_names

#data.keys()
#data1 = data.loc[:, ['targetTrial', 'force_L','force_R','fliptime', 'time','targets','target_names']]




#%% Save the data file 
import os
import datetime, time 
timestamp=time.time()
timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H%M')

save_in = os.path.split(filepath)[0]

save_it_as_pkl = os.path.join(save_in,str("DATA_file_"+timestamp_readable+".pkl"))
data.to_pickle(save_it_as_pkl)




#%% plot all trials individually 
# data.drop(data[data['dropindex']==True].index, inplace=True)
# data.drop("dropindex",1,inplace=True)
import matplotlib.pyplot as plt 
%matplotlib inline
trial_keys = data['targetTrial'].index
for i in range(len(trial_keys)) : 
    title = data.loc[trial_keys[i],'targetTrial']
    # force_L_1 = data.loc[trial_keys[1],'force_L']
    # target_L_1 = data.loc[trial_keys[1],'targets']
    t_1 = data.loc[trial_keys[i],'time']
    force_R_1 = data.loc[trial_keys[i],'force_R']
    target_R_1 = data.loc[trial_keys[i],'targets']
    
    plt.figure(i)
    plt.plot(t_1,force_R_1)
    plt.plot(t_1,target_R_1)
    plt.title(title)






#%% Combining into conditions 

data_con = pd.DataFrame()

for i in range(len(data['dropindex'])):
    

data_con = data['dropindex'][]==False 


conds_ = targets_

data1 = data.loc[:, ['targetTrial', 'force_L','force_R','fliptime', 'time','targets','target_names']]



#%% Making a new dataframe easier to work with 
trial_no = file['trial'][0] 
trial_shifts = file['save_trialshift'][0] # [trial, targets_names[conditions[trial]], onsets[trial], durations[trial], globalClock.getTime()-t0, t]

data = pd.DataFrame()
indices = []
targets_, onsets_, durations_, t_ = [],[],[],[]
for j in range(len(trial_shifts)): 
    targets_.append(str(trial_shifts[j][1]))
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
#data.drop(data[data['dropindex']==True].index, inplace=True )
#data.drop("dropindex",1,inplace=True)


#%% 
import numpy as np
force_L, force_R, v_mean, time, fliptime, target_names, targets = [],[], [], [],[], [],[]
test_unique = []
for j in range(len(trial_shifts)):
    idx = data.loc[j,'indices']
    force_L.append(file['left_force'][0][min(idx):max(idx)+1])
    force_R.append(file['right_force'][0][min(idx):max(idx)+1])
    #v.append(file['appleJack_raw'][0][min(idx):max(idx)+1])
    #v_mean.append(file['appleJack_smoothed'][0][min(idx):max(idx)+1])
    time.append(file['time'][0][min(idx):max(idx)+1])
    fliptime.append(file['fliptime'][0][min(idx):max(idx)+1])
    target_names.append(file['target_name'][0][min(idx):max(idx)+1])
    targets.append(file['target'][0][min(idx):max(idx)+1])
    test_unique.append(np.unique(file['target_name'][0][min(idx):max(idx)+1]))
    
data['force_L'] = force_L
data['force_R'] = force_R
#data['appleJack_raw'] = v
#data['appleJack_smoothed'] = v_mean
data['time'] = time
data['fliptime'] = fliptime
data['targets'] = targets
data['target_names'] = target_names



















