# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:19:22 2021

@author: dzn332
"""

#%%
import os 
# Specify path to DATA
path = os.path.join('C:\\','Users','dzn332','Documents','DYBICO','DATA')
os.chdir(os.path.split(path)[0])

# specify list of subjects 
list_of_subjs = ['test_20211206'] 


#%% run pre-processing loop
import postproc_helper as pph 
(maxforce, settings, data_file, filepath) = pph.preproc_loop(list_of_subjs, path)
os.chdir(path)


#%% run post processing loop over list of subjs 
import pandas as pd 
import postproc_helper as pph 
import matplotlib.pyplot as plt

for i in range(len(list_of_subjs)):
    # Specify log ID
    log = list_of_subjs[i]
    
    # read all data files from folder
    DATAfiles = pph.get_DATAfiles(os.path.join(path,log))
    
    for k in range(len(DATAfiles)):
        datafile = DATAfiles[k]  
        filepath = os.path.join(path,log,'PostProcessing',datafile)
        
        # read the file
        file=pd.read_pickle(filepath)
        data = pph.drop_non_trials(file)
        con_matrix = pph.sort_data_by_condition(data) 
        
        for c in range(len(con_matrix)):
            con_data = con_matrix[c]
            con_data.index = range(len(con_data)) 
            #pph.make_cond_folder(filepath, con_data) 
            saveID = str(con_data['targetTrial'][0])+"_"+str(os.path.split(filepath)[1][12:-4])

            # extract data traces as arrays
            (shortest_trial, force_L, force_R, target_L, target_R, time) = pph.extract_as_arrays(con_data)
            
            # calculate averages
            avg_L = force_L.mean(axis=0)
            avg_R = force_R.mean(axis=0)
            avg_target_L = target_L.sum(axis=0)/len(target_L)
            avg_target_R = target_R.sum(axis=0)/len(target_R)
            t = [(time[j]-time[j][0]) for j in range(len(time))][0]
            
            # insert stuff to calculate reaction time & accuracy 
            
            # plot 
            plt.figure(c)
            plt.plot(t,avg_R, label="Right force")
            plt.plot(t,avg_target_R, label="Right target")
            plt.plot(t,avg_L, label="Left force")
            plt.plot(t,avg_target_L, label="Left target")
            plt.title(con_data['targetTrial'][0])
            plt.legend()
            plt.xlabel('Seconds')
            plt.ylabel('Maxforce')
            plt.yticks([0.25, 0.5, 0.75], ['2.5%', '5%', '7.5%'])
            #plt.show()

            # save the figure 
            os.chdir(os.path.join(os.path.split(filepath)[0]))
            plt.savefig(saveID+'.png')
            plt.clf()
            
os.chdir(os.path.join('C:\\','Users','dzn332','Documents','DYBICO'))
            
            
            
            
            
            
            
            

























