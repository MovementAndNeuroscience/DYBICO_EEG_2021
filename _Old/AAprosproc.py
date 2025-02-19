# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:21:56 2021

@author: dzn332
"""


#%% Specify file 
import os 
import sys
# Specify path to DATA
path = os.path.join('C:\\','Users','dzn332','Documents','D-BICO','DATA')

# Specify log ID
log = 'P001'

# Specify data to work with 
datafile = 'DATA_file_20211123_1224.pkl'#'output_file_20211123_1138.pkl' #'DATA_file_20211123_1224.pkl'

filepath = os.path.join(path,log,datafile)





#%% 


#%% Read the file 
import pandas as pd 
file=pd.read_pickle(filepath)
# file.keys() # to see what information is in the file 
# settings = file['settings'][0]

# we now change the directory to the post-proc folder for saving 
os.chdir(PPpath)

#%% drop all non-trials, i.e. pauses 
data = file.copy()
data.drop(data[data['dropindex']==True].index, inplace=True) 
data.drop("dropindex",1,inplace=True)
data.index = range(len(data)) 


#%% make list of all conditions, and a list of which conditions 
import numpy as np 
conditions = []
for i in range(len(data['targetTrial'])):
    conditions.append(np.unique(data['target_names'][i])[0])
ucon = np.unique(conditions)
print(ucon)
   
    
#%% make dummy variables specific for all the included conditions
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
    data_name = str(ucon[i]) 
    con_matrix.append(data[dummies[d_name]==1])

    
#%% 
import matplotlib.pyplot as plt

for i in range(len(con_matrix)):
    con_data = con_matrix[i]
    con_data.index = range(len(con_data)) 

    # we find the shortest trial lenght (due to jitter time inconsistencies)
    shortest_trial = min([len(con_data['targets'][j]) for j in range(len(con_data))])
        
    # we extract the force and find the average trace 
    force_L = np.vstack([np.asarray(con_data['force_L'][j][:shortest_trial]) for j in range(len(con_data))])
    force_R = np.vstack([np.asarray(con_data['force_R'][j][:shortest_trial]) for j in range(len(con_data))])
    avg_L = force_L.mean(axis=0)
    avg_R = force_R.mean(axis=0)
   
    # jittertime in onset/dur, makes to baseline vary between point 114 and 122. 
    t_L, t_R  = [], []
    for j in range(len(con_data)) : 
        t_L.append([np.asarray(con_data['targets'][j][k][0]) for k in range(shortest_trial)])
        t_R.append([np.asarray(con_data['targets'][j][k][1]) for k in range(shortest_trial)])
    target_L = (np.vstack(t_L)).sum(axis=0)/len(t_L)
    target_R = (np.vstack(t_R)).sum(axis=0)/len(t_R)

    # we adjust target to an average
    #target_Lsum = target_L.sum(axis=0)/len(con_data['targets']) 
    #target_Rsum = target_R.sum(axis=0)/len(con_data['targets'])
    
    # get time data 
    time = np.vstack([np.asarray(con_data['time'][j][:shortest_trial]) for j in range(len(con_data))]) 
    t = [(time[j]-time[j][0]) for j in range(len(time))][0]

    
    #os.chdir(PPpath) 
    
    # plot 
    title = con_data['target_names'][0][0]
    plt.figure(i)
    plt.plot(t,avg_R, label="Right force")
    plt.plot(t,target_R, label="Right target")
    plt.plot(t,avg_L, label="Left force")
    plt.plot(t,target_L, label="Left target")
    plt.title(title)
    plt.legend()
    plt.xlabel('Seconds')
    plt.ylabel('Maxforce')
    plt.yticks([0.25, 0.5, 0.75], ['2.5%', '5%', '7.5%'])
    #plt.ylim([0,1])
    
    

    # save figures
    # save new dataframes for each cond :
        # with force, targets, time, before and after averaging  
    
    # new post-proc folder in each subject 
    #plt.savefig('books_read.png')
    
    
    
    
    
    
    
    
    
    
    
#%% 












