# -*- coding: utf-8 -*-
"""
"""

import pandas 
import numpy 
import os

L_files = ['./L_00','./L_100','./L_200','./L_300','./L_400','./L_500','./L_600','./L_700','./L_1000']
R_files = ['./R_00','./R_100','./R_200','./R_300','./R_400','./R_500','./R_600','./R_700','./R_1000']

path = os.path.join('C:\\','Users','dzn332','Documents','DYBICO','Calibration','dec21')


left_y = []
left_x = []
for i in range(len(L_files)):
    os.chdir(os.path.join(path,'left_20211206', 'Maxforce'))
    L1=pandas.read_pickle(L_files[i])['Left']#[17:]
    
    X_L1=numpy.mean(L1)
    left_x.append([0])
    left_y.append([X_L1])
    xL_save=numpy.concatenate(left_x)
    yL_save=numpy.concatenate(left_y)
    
    save_as = str(L_files[i][2:]+'.npy')
    save_in = os.path.join(os.path.split(path)[0],'Calibration',save_as)
    numpy.save(save_in, [xL_save,yL_save])

    

right_y = []
right_x = []
for i in range(len(R_files)):
    os.chdir(os.path.join(path,'right_20211206', 'Maxforce'))
    R1=pandas.read_pickle(R_files[i])['right']#[17:]
    
    X_R1=numpy.mean(R1)
    right_x.append([0])
    right_y.append([X_R1])
    xR_save=numpy.concatenate(right_x)
    yR_save=numpy.concatenate(right_y)
    
    save_as = str(R_files[i][2:]+'.npy')
    save_in = os.path.join(os.path.split(path)[0],'Calibration',save_as)
    numpy.save(save_in, [xR_save,yR_save])




#%%












