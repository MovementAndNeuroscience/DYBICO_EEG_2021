# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:40:34 2021

@author: dzn332
"""

L1FAKE=pd.read_pickle('C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/DATA/LASSE_20210921/Maxforce/maxforceL1')['Left']
L2FAKE=pd.read_pickle('C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/DATA/LASSE_20210921/Maxforce/maxforceL2')['Left']
L3FAKE=pd.read_pickle('C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/DATA/LASSE_20210921/Maxforce/maxforceL3')['Left']

R1FAKE=pd.read_pickle('C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/DATA/LASSE_20210921/Maxforce/maxforceR1')['Right']
R2FAKE=pd.read_pickle('C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/DATA/KEENIE_20210921 (excl. time collected)/Maxforce/maxforceR2')['Right']
R3FAKE=pd.read_pickle('C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/DATA/LASSE_20210921/Maxforce/maxforceR3')['Right']



# Make dataframe 
import pandas as pd 
maxforces = pd.DataFrame()
maxforces['Left']=v_left
maxforces['Right']=R3FAKE[:657] 
maxforces['TrialType']=v_type
maxforces['Time']=t_save
maxforces['Fliptime']=t_flip 

mfdir='C:\\Users\dzn332\Documents\GitHub\BIMANUAL_KAA21\DATA\FAKE'
savename='maxforceR3_FAKE'

maxforces.to_pickle(mfdir+str("/")+savename) 
print('\n_____________________\n \n SAVED %s  \n_____________________\n' %savename)
    





