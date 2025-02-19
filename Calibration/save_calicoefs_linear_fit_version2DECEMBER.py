# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:59:40 2021
@author: dzn332

Calibration file creator 
"""

import pandas as pd 
import numpy as np
import os

path = os.path.join('C:\\','Users','dzn332','Documents','DYBICO','Calibration','dec21')
os.chdir(path)

l,Lu=[],[]
r,Ru=[],[]
for filename in os.listdir(path):
        if filename[0] == 'L' :
            l.append(int(filename[2:]))
            Lu.append(np.mean(np.array(pd.read_pickle(os.path.join(path,filename))['Left'][0][20:])))
        if filename[0] == 'R' :
            r.append(int(filename[2:]))
            Ru.append(np.mean(np.array(pd.read_pickle(os.path.join(path,filename))['Right'][0][20:])))
l=np.array(l)
r=np.array(r)
Ru=np.array(Ru)
Lu=np.array(Lu)


import matplotlib.pyplot as plt 
plt.scatter(l, Lu, c='b', label='left')
plt.scatter(r, Ru, c='r', label='right')
plt.legend()


#%%
import numpy as np 
import matplotlib.pyplot as plt 

yr=(r.reshape(-1,1)/1000)*9.815 
Xr=Ru.reshape(-1,1)
yl=(l.reshape(-1,1)/1000)*9.815 
Xl=Lu.reshape(-1,1)
X_plot = np.linspace(0, 2000, 1000)[:, None]

from sklearn.linear_model import LinearRegression
regR = LinearRegression().fit(Xr, yr)
coefR=regR.score(Xr, yr)
y_gprR = regR.predict(X_plot)
regL = LinearRegression().fit(Xl, yl) 
coefL=regL.score(Xl, yl)
y_gprL = regL.predict(X_plot)


# Plot results
plt.figure(figsize=(10, 5))
lw = 2
plt.scatter(Xr, yr, c='y', label='right')
plt.scatter(Xl, yl, c='r', label='left')
plt.plot(X_plot, y_gprR, color='yellow', lw=lw,
         label='Right')
plt.plot(X_plot, y_gprL, color='red', lw=lw,
         label='Left')
plt.xlabel('raw units')
plt.ylabel('[Newtons]')
plt.title('Left Hand: coef: %.4f   Right Hand: coef: %.4f' %(coefL, coefR))
plt.legend(loc="best",  scatterpoints=1)
plt.ylim(-1,50)
plt.xlim(-1,700)
plt.show()

coefs = [regL.coef_[0], regL.intercept_, regR.coef_[0], regR.intercept_]
np.save(os.path.join('C:\\','Users','dzn332','Documents','DYBICO','Calibration','calicoefs.npy'), coefs)
print(regL.coef_[0], regL.intercept_, regR.coef_[0], regR.intercept_)

#%%

calipath = os.path.join('C:\\','Users','dzn332','Documents','DYBICO','Calibration','calicoefs_sep2021.npy')
[Lcoef, Lint, Rcoef, Rint]=np.load(calipath) 
print(Lcoef, Lint, Rcoef, Rint)

#%%