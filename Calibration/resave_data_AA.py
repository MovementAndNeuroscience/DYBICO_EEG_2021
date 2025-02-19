# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:46:36 2021

@author: Adrien
"""

import pandas 
import numpy 
import os
import matplotlib.pyplot as plt
left_y = []
left_x = []

right_y = []
right_x = []

os.chdir("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/leftmax3_20211020/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]

os.chdir("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/rightmax3_20211020/Maxforce")
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]

X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([0, 0, 0])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([0, 0, 0])
right_y.append([X_R1,X_R2, X_R3])



xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/thirdday/left5000w.npy", [xL_save,yL_save])

xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)
numpy.save("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/thirdday/right5000W.npy", [xR_save,yR_save])


#%%












left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w100_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([100, 100, 100])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([100, 100, 100])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left100W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right100W.npy", [xR_save,yR_save])








left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w200_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([200, 200, 200])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([200, 200, 200])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left200W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right200W.npy", [xR_save,yR_save])













left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w300_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([300, 300, 300])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([300, 300, 300])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left300W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right300W.npy", [xR_save,yR_save])



left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w400_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([400, 400, 400])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([400, 400, 400])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left400W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right400W.npy", [xR_save,yR_save])














left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w500_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([500, 500, 500])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([500, 500, 500])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left500W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right500W.npy", [xR_save,yR_save])











left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w600_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([600, 600, 600])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([600, 600, 600])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left600W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right600W.npy", [xR_save,yR_save])























left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w700_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([700, 700, 700])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([700, 700, 700])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left700W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right700W.npy", [xR_save,yR_save])









left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w1000_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([1000, 1000, 1000])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([1000, 1000, 1000])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left1000W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right1000W.npy", [xR_save,yR_save])





left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w1500_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([1500, 1500, 1500])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([1500, 1500, 1500])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left1500W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right1500W.npy", [xR_save,yR_save])






left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w2000_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([2000, 2000, 2000])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([2000, 2000, 2000])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left2000W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right2000W.npy", [xR_save,yR_save])





left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w2500_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([2500, 2500, 2500])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([2500, 2500, 2500])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left2500W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right2500W.npy", [xR_save,yR_save])






left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w3000_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([3000, 3000, 3000])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([3000, 3000, 3000])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left3000W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right3000W.npy", [xR_save,yR_save])




left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w3500_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([3500, 3500, 3500])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([3500, 3500, 3500])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left3500W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right3500W.npy", [xR_save,yR_save])






left_y = []
left_x = []

right_y = []
right_x = []


#%%
os.chdir("C://Users/anazv/Desktop/calibration_data/1/w4000_20210929/Maxforce")
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_L1=numpy.mean(L1)
X_L2=numpy.mean(L2)
X_L3=numpy.mean(L3)
X_R1=numpy.mean(R1)
X_R2=numpy.mean(R2)
X_R3=numpy.mean(R3)

left_x.append([4000, 4000, 4000])
left_y.append([X_L1,X_L2, X_L3])

right_x.append([4000, 4000, 4000])
right_y.append([X_L1,X_L2, X_L3])


#%%
xL_save=numpy.concatenate(left_x)
yL_save=numpy.concatenate(left_y)
numpy.save("C://Users/anazv/Desktop/calibration_data/left4000W.npy", [xL_save,yL_save])


xR_save=numpy.concatenate(right_x)
yR_save=numpy.concatenate(right_y)


numpy.save("C://Users/anazv/Desktop/calibration_data/right4000W.npy", [xR_save,yR_save])























os.chdir('C://Users/anazv/Desktop/calibration_data/1/00w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_100L1=numpy.mean(L1)
X_100L2=numpy.mean(L2)
X_100L3=numpy.mean(L3)
X_100R1=numpy.mean(R1)
X_100R2=numpy.mean(R2)
X_100R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L100=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R100=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/1/w200w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_200L1=numpy.mean(L1)
X_200L2=numpy.mean(L2)
X_200L3=numpy.mean(L3)
X_200R1=numpy.mean(R1)
X_200R2=numpy.mean(R2)
X_200R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L200=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R200=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/300w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_300L1=numpy.mean(L1)
X_300L2=numpy.mean(L2)
X_300L3=numpy.mean(L3)
X_300R1=numpy.mean(R1)
X_300R2=numpy.mean(R2)
X_300R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L300=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R300=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/400w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_400L1=numpy.mean(L1)
X_400L2=numpy.mean(L2)
X_400L3=numpy.mean(L3)
X_400R1=numpy.mean(R1)
X_400R2=numpy.mean(R2)
X_400R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L400=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R400=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/500w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_500L1=numpy.mean(L1)
X_500L2=numpy.mean(L2)
X_500L3=numpy.mean(L3)
X_500R1=numpy.mean(R1)
X_500R2=numpy.mean(R2)
X_500R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L500=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R500=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/600w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_600L1=numpy.mean(L1)
X_600L2=numpy.mean(L2)
X_600L3=numpy.mean(L3)
X_600R1=numpy.mean(R1)
X_600R2=numpy.mean(R2)
X_600R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L600=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R600=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/700w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_700L1=numpy.mean(L1)
X_700L2=numpy.mean(L2)
X_700L3=numpy.mean(L3)
X_700R1=numpy.mean(R1)
X_700R2=numpy.mean(R2)
X_700R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L700=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R700=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/1000w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_1000L1=numpy.mean(L1)
X_1000L2=numpy.mean(L2)
X_1000L3=numpy.mean(L3)
X_1000R1=numpy.mean(R1)
X_1000R2=numpy.mean(R2)
X_1000R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L1000=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R1000=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/1500w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_1500L1=numpy.mean(L1)
X_1500L2=numpy.mean(L2)
X_1500L3=numpy.mean(L3)
X_1500R1=numpy.mean(R1)
X_1500R2=numpy.mean(R2)
X_1500R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L1500=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R1500=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/2000w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_2000L1=numpy.mean(L1)
X_2000L2=numpy.mean(L2)
X_2000L3=numpy.mean(L3)
X_2000R1=numpy.mean(R1)
X_2000R2=numpy.mean(R2)
X_2000R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L2000=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R2000=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/2500w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_2500L1=numpy.mean(L1)
X_2500L2=numpy.mean(L2)
X_2500L3=numpy.mean(L3)
X_2500R1=numpy.mean(R1)
X_2500R2=numpy.mean(R2)
X_2500R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L2500=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R2500=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/3000w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_3000L1=numpy.mean(L1)
X_3000L2=numpy.mean(L2)
X_3000L3=numpy.mean(L3)
X_3000R1=numpy.mean(R1)
X_3000R2=numpy.mean(R2)
X_3000R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L3000=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R3000=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/3500w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_3500L1=numpy.mean(L1)
X_3500L2=numpy.mean(L2)
X_3500L3=numpy.mean(L3)
X_3500R1=numpy.mean(R1)
X_3500R2=numpy.mean(R2)
X_3500R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L3500=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R3500=(R1+R2+R3)/3

os.chdir('C://Users/anazv/Desktop/calibration_data/2/4000w_20211004/Maxforce')
L1=pandas.read_pickle('./maxforceL1')['Left'][17:]
L2=pandas.read_pickle('./maxforceL2')['Left'][17:]
L3=pandas.read_pickle('./maxforceL3')['Left'][17:]
R1=pandas.read_pickle('./maxforceR1')['Right'][17:]
R2=pandas.read_pickle('./maxforceR2')['Right'][17:]
R3=pandas.read_pickle('./maxforceR3')['Right'][17:]
X_4000L1=numpy.mean(L1)
X_4000L2=numpy.mean(L2)
X_4000L3=numpy.mean(L3)
X_4000R1=numpy.mean(R1)
X_4000R2=numpy.mean(R2)
X_4000R3=numpy.mean(R3)
L1=max(L1)-min(L1)
L2=max(L2)-min(L2)
L3=max(L3)-min(L3)
L4000=(L1+L2+L3)/3
R1=max(R1)-min(R1)
R2=max(R2)-min(R2)
R3=max(R3)-min(R3)
R4000=(R1+R2+R3)/3


#%%
keenie 





#%% 





#averages of the averages
X_000R=(X_000R1+X_000R2+X_000R3)/3
X_100R=(X_100R1+X_100R2+X_100R3)/3
X_200R=(X_200R1+X_200R2+X_200R3)/3
X_300R=(X_300R1+X_300R2+X_300R3)/3
X_400R=(X_400R1+X_400R2+X_400R3)/3
X_500R=(X_500R1+X_500R2+X_500R3)/3
X_600R=(X_600R1+X_600R2+X_600R3)/3
X_700R=(X_700R1+X_700R2+X_700R3)/3
X_1000R=(X_1000R1+X_1000R2+X_1000R3)/3
X_1500R=(X_1500R1+X_1500R2+X_1500R3)/3
X_2000R=(X_2000R1+X_2000R2+X_2000R3)/3
X_2500R=(X_2500R1+X_2500R2+X_2500R3)/3
X_3000R=(X_3000R1+X_3000R2+X_3000R3)/3
X_3500R=(X_3500R1+X_3500R2+X_3500R3)/3
X_4000R=(X_4000R1+X_4000R2+X_4000R3)/3


X_000L=(X_000L1+X_000L2+X_000L3)/3
X_100L=(X_100L1+X_100L2+X_100L3)/3
X_200L=(X_200L1+X_200L2+X_200L3)/3
X_300L=(X_300L1+X_300L2+X_300L3)/3
X_400L=(X_400L1+X_400L2+X_400L3)/3
X_500L=(X_500L1+X_500L2+X_500L3)/3
X_600L=(X_600L1+X_600L2+X_600L3)/3
X_700L=(X_700L1+X_700L2+X_700L3)/3
X_1000L=(X_1000L1+X_1000L2+X_1000L3)/3
X_1500L=(X_1500L1+X_1500L2+X_1500L3)/3
X_2000L=(X_2000L1+X_2000L2+X_2000L3)/3
X_2500L=(X_2500L1+X_2500L2+X_2500L3)/3
X_3000L=(X_3000L1+X_3000L2+X_3000L3)/3
X_3500L=(X_3500L1+X_3500L2+X_3500L3)/3
X_4000L=(X_4000L1+X_4000L2+X_4000L3)/3




#plotting

y = [X_000R, X_100R, X_200R, X_300R, X_400R, X_500R, X_600R, X_700R, X_1000R, X_1500R, X_2000R, X_2500R, X_3000R, X_3500R, X_4000R]
x = [4, 110, 215, 301, 396, 492, 603, 702, 1002, 1487, 1993, 2506, 3004, 3504, 3991]
plt.plot(x, y,label = "Right", color='red', markerfacecolor='red')
Y = [R0, R100, R200, R300, R400, R500, R600, R700, R1000, R1500, R2000, R2500, R3000, R3500, R4000]
plt.plot(x, Y,label = "Right", color='red', markerfacecolor='red')
y2 = [X_000L, X_100L, X_200L, X_300L, X_400L, X_500L, X_600L, X_700L, X_1000L, X_1500R, X_2000L, X_2500L, X_3000L, X_3500L, X_4000L]
x2 = [0, 98, 196, 301, 407, 500, 600, 706, 1012, 1488, 2000, 2483, 3007, 3480, 3990]
plt.plot(x2, y2, color='green',label = "Left", markerfacecolor='green')
Y2 = [L0, L100, L200, L300, L400, L500, L600, L700, L1000, L1500, L2000, L2500, L3000, L3500, L4000]
plt.plot(x2, Y2, color='green',label = "Left", markerfacecolor='green')
plt.xlabel('Weight (grams)')
plt.ylabel('Millivolts')
plt.title('Right and left devices output')
plt.show()