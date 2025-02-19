# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:27:24 2021

@author: dzn332
"""


#%% drop non-trials 
def drop_non_trials(file):
    # drop all non-trials, i.e. pauses 
    data = file.copy()
    data.drop(data[data['dropindex']==True].index, inplace=True) 
    data.drop("dropindex",1,inplace=True)
    data.index = range(len(data)) 
    
    return data 



#%% sort the data
def sort_data_by_condition(data):
    # list unique conditions & list of conditions 
    import numpy as np
    conditions = data['targetTrial']
    ucon = np.unique(conditions)
    
    # make dummy variables specific for all the included conditions
    import pandas as pd 
    dummies=pd.DataFrame()
    con_matrix = []
    for i in range(len(ucon)):
        d_name = str('d_'+ucon[i])
        dummy=[]
        for j in range(len(conditions)):
            if conditions[j]==ucon[i]:
                dummy.append(1)
            else:
                dummy.append(0)
        dummies[d_name]=dummy
        con_matrix.append(data[dummies[d_name]==1])
        
    return con_matrix 



#%% extract force and target and time data 
def extract_as_arrays(con_data):
    # we find the shortest trial lenght (due to jitter time inconsistencies)
    shortest_trial = min([len(con_data['targets'][j]) for j in range(len(con_data))])
    
    # we extract the force and find the average trace 
    import numpy as np 
    force_L = np.vstack([np.asarray(con_data['force_L'][j][:shortest_trial]) for j in range(len(con_data))])
    force_R = np.vstack([np.asarray(con_data['force_R'][j][:shortest_trial]) for j in range(len(con_data))])
    
    # jittertime in onset/dur, makes to baseline vary between point 114 and 122. 
    t_L, t_R  = [], []
    for j in range(len(con_data)) : 
        t_L.append([np.asarray(con_data['targets'][j][k][0]) for k in range(shortest_trial)])
        t_R.append([np.asarray(con_data['targets'][j][k][1]) for k in range(shortest_trial)])
    target_L = np.vstack(t_L)
    target_R = np.vstack(t_R)
    
    # get time data 
    time = np.vstack([np.asarray(con_data['time'][j][:shortest_trial]) for j in range(len(con_data))]) 

    
    return (shortest_trial, force_L, force_R, target_L, target_R, time)
    


#%% get list of DATA files in log folder
def get_DATAfiles(logdir):
    import os 
    os.chdir(os.path.join(logdir,'PostProcessing'))
    
    import glob
    DATAfiles = []
    for file in glob.glob("DATA_file*.pkl"):
        DATAfiles.append(file)
    
    return DATAfiles



#%% Make a folder for each condition
def make_cond_folder(filepath, con_data):
    import os 
    title = con_data['targetTrial'][0]
    os.chdir(os.path.split(filepath)[0])
    if not os.path.exists(title): os.makedirs(title)

    

#%% save figure 
# def save_fig(filepath,con_data,saveID):
#     import os 
#     title = con_data['targetTrial'][0]
#     os.chdir(os.path.join(os.path.split(filepath)[0]))

#     import matplotlib.pyplot as plt    
#     plt.savefig(saveID+'.png')
    
    # save variables: force, targets, time, before and after averaging 
    # import numpy as np
    # cond_data = np.vstack([force_L, force_R, target_L, target_R, time])
    # np.savetxt(saveID+".npy", cond_data, delimiter=",")
    # os.chdir(os.path.split(filepath)[0])               
    


#%%












#%% run loop across list of subjs 
def preproc_loop(list_of_subjs, path):
    import postproc_helper as pph 
    import os 
    
    for i in range(len(list_of_subjs)):
        # Specify log ID
        log = list_of_subjs[i]
        
        # read all output files from folder
        outputfiles = pph.get_outputfiles(os.path.join(path,log))
        
        for k in range(len(outputfiles)):
            datafile = outputfiles[k]   # Specify data to work with  'DATA_file_20211123_1224.pkl'#'output_file_20211123_1138.pkl' #'DATA_file_20211123_1224.pkl'
            filepath = os.path.join(path,log,datafile)
            
            # make directory structure 
            pph.make_PP_folder(filepath)
            
            # save tables.png with info on settings
            settings = pph.print_settings(filepath)
            
            # get maxforce for that subj 
            maxforce = pph.get_maxforce(filepath)
            
            # reshape the data and save as file 
            data_file = pph.reshape_data(filepath)
            
    return (maxforce, settings, data_file, filepath)



#%% get list of output files in log folder
def get_outputfiles(logdir):
    import os 
    os.chdir(logdir)
    
    import glob
    outputfiles = []
    for file in glob.glob("output_file*.pkl"):
        outputfiles.append(file)
    
    if len(outputfiles)<3 : 
        print('ERROR NOT ENOUGH OUTPUT FILES, CHECK FOLDER')
    elif len(outputfiles)>3 : 
        print('ERROR TOO MANY OUTPUT FILES, CHECK FOLDER')
    
    return outputfiles



#%% Make a folder for post processing data
def make_PP_folder(filepath):
    import os 
    logpath = os.path.split(filepath)[0]
    os.chdir(logpath)
    
    if not os.path.exists('PostProcessing'): os.makedirs('PostProcessing')
    #PPpath=os.path.join(logpath,'PostProcessing')
    #return PPpath 



#%% print settings out in figure 
def print_settings(filepath):
    import pandas as pd 
    file=pd.read_pickle(filepath) # load file 
    
    settings = file['settings'][0]
    settings_cond = settings.loc[:, ['Baseline_force', 'Left_increase_force', 'Left_decrease_force',
       'Right_increase_force', 'Right_decrease_force', 'Sym_increase_force',
       'Sym_decrease_force', 'Asym_L_increase_R_decrease',
       'Asym_L_decrease_R_increase']]
    settings_ = settings.loc[:, ['no_of_blocks', 'time_between_blocks',
       'trial_repetitions', 'trial_duration', 'jitter_time',
       'baseline_between_trials', 'percent_change_from_baseline',
       'percent_of_maxforce', 'smoothing']]
    
    
    # save figures with information
    import os
    os.chdir(os.path.join(os.path.split(filepath)[0],'PostProcessing'))
    import dataframe_image as dfi # pip install dataframe_image
    df_styled = settings_.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(df_styled,"table_of_settings.png")
    df_styled = settings_cond.style.background_gradient() #adding a gradient based on values in cell
    dfi.export(df_styled,"table_of_conditions.png")
    os.chdir(os.path.split(filepath)[0])
    
    return settings 



#%% print out maxforce from 
def get_maxforce(filepath):
    import pandas as pd 
    file=pd.read_pickle(filepath) #% load file 

    # print out maxforce 
    maxforce = file['maxforceLR'][0]
    
    # save as csv file
    import os 
    os.chdir(os.path.join(os.path.split(filepath)[0],'PostProcessing'))
    import numpy as np   
    np.savetxt("maxforce.csv", np.asarray(maxforce), delimiter=",")
    #np.loadtxt("maxforce.csv") 
    os.chdir(os.path.split(filepath)[0])
    
    return maxforce



#%% reshape output file to data file structure 
def reshape_data(filepath): # change output file structure  
    import pandas as pd 
    file=pd.read_pickle(filepath) #% load file 

    # first we rearrange single-entry data per trial 
    trial_no = file['trial'][0] 
    trial_shifts = file['save_trialshift'][0] 
    data = pd.DataFrame()
    targets_, onsets_, durations_, t_, indices = [], [],[],[],[]
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
    
    # We mark intermediate data ie pauses, in this new dataframe 
    dropindex = []
    for j in range(len(trial_shifts)): 
        dropindex.append(data['targetTrial'][j][:5] =='Pause')
        if dropindex[j] == False : dropindex[j] = data['duration'][j]==0.5000 
    data['dropindex']=dropindex
    #data.drop(data[data['dropindex']==True].index, inplace=True) 
    #data.drop("dropindex",1,inplace=True)
    #data.index = range(len(data)) 

    # we then use indices calculated previously, to sort arrays in trials
    import numpy as np
    force_L, force_R, time, fliptime, target_names, targets = [], [], [],[], [],[]
    #test_unique = [] # only to ensure the code was correct 
    for j in range(len(trial_shifts)):
        idx = data.loc[j,'indices']
        force_L.append(file['left_force'][0][min(idx):max(idx)+1])
        force_R.append(file['right_force'][0][min(idx):max(idx)+1])
        time.append(file['time'][0][min(idx):max(idx)+1])
        targets.append(file['target'][0][min(idx):max(idx)+1])
        #fliptime.append(file['fliptime'][0][min(idx):max(idx)+1])
        #target_names.append(file['target_name'][0][min(idx):max(idx)+1])
        #test_unique.append(np.unique(file['target_name'][0][min(idx):max(idx)+1]))
    data['force_L'] = force_L
    data['force_R'] = force_R
    data['time'] = time
    data['targets'] = targets
    #data['fliptime'] = fliptime # about 31 millisecond difference 
    #data['target_names'] = target_names
    
    
    # Save the data file 
    import os
    PPpath = os.path.join(os.path.split(filepath)[0],'PostProcessing')
    logID = os.path.split(filepath)[1][12:-4]
    save_it_as_pkl = os.path.join(PPpath,str("DATA_file_"+logID+".pkl"))
    data.to_pickle(save_it_as_pkl)
    
    return data 
    
    
    
#%%     





































