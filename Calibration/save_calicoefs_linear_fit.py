# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 21:59:40 2021
@author: dzn332

Calibration file creator 
"""

#%%
# reads the files with the data
import numpy as np 
import os 
paths=["C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/firstday",
       "C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/secondday",
       "C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/new_data/thirdday"]
l,L1w,L1u=[],[],[]
r,R1w,R1u=[],[],[]
for i in range(3):
    path = paths[i]
    for filename in os.listdir(path):
        if filename[0] == 'l' :
            l.append(filename)
            L1w.append(np.load(os.path.join(path,filename))[0])
            L1u.append(np.load(os.path.join(path,filename))[1])
        if filename[0] == 'r' :
            r.append(filename)
            R1w.append(np.load(os.path.join(path,filename))[0])
            R1u.append(np.load(os.path.join(path,filename))[1])

# correct the maxforce add-on
L1w[12]=[5000,5000,5000]
R1w[12]=[5000,5000,5000]
L1w[28]=[5000,5000,5000]
R1w[28]=[5000,5000,5000]
L1w[44]=[5000,5000,5000]
R1w[44]=[5000,5000,5000]

# remove extra data (error from saving)
L1w[41]=L1w[41][:3]
R1w[41]=R1w[41][:3]
L1u[41]=L1u[41][:3]
R1u[41]=R1u[41][:3]

# change array formats
w_l = np.concatenate(L1w)
W_l = w_l.reshape(-1, 1)
u_l = np.concatenate(L1u)
w_r = np.concatenate(R1w)
W_r = w_r.reshape(-1, 1)
u_r = np.concatenate(R1u)


import matplotlib.pyplot as plt 
plt.scatter(W_l, u_l, c='b', label='left')
plt.scatter(W_r, u_r, c='r', label='right')
plt.legend()

import pandas as pd 
rawUnits_LR = pd.DataFrame()
rawUnits_LR['Weights_l'] = [W_l.flatten()]
rawUnits_LR['Weights_r'] = [W_r.flatten()]
rawUnits_LR['u_l']=[u_l]
rawUnits_LR['u_r']=[u_r]
rawUnits_LR['list_left']=[l]
rawUnits_LR['list_right']=[r]
rawUnits_LR.to_pickle("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/rawUnits_LR.pkl")





#%%
import pandas as pd 
rawUnits_LR = pd.read_pickle("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/rawUnits_LR.pkl")

W_l=rawUnits_LR['Weights_l'][0]
W_r=rawUnits_LR['Weights_r'][0]
u_l=rawUnits_LR['u_l'][0]
u_r=rawUnits_LR['u_r'][0]
l=rawUnits_LR['list_left'][0]
r=rawUnits_LR['list_right'][0]



#%%
import numpy as np 
import matplotlib.pyplot as plt 

yr=(W_r.reshape(-1,1)/1000)*9.815 
Xr=u_r.reshape(-1,1)
yl=(W_l.reshape(-1,1)/1000)*9.815 
Xl=u_l.reshape(-1,1)
X_plot = np.linspace(0, 2000, 1000)[:, None]

from sklearn.linear_model import LinearRegression
regR = LinearRegression().fit(Xr, yr)
coefR=regR.score(Xr, yr)
y_gprR = regR.predict(X_plot)

regL = LinearRegression().fit(Xl, yl) #fit_intercept=False
coefL=regL.score(Xl, yl)
y_gprL = regL.predict(X_plot)


# Plot results
plt.figure(figsize=(10, 5))
lw = 2
plt.scatter(Xr, yr, c='y', label='right')
plt.scatter(Xl, yl, c='r', label='left')
plt.plot(X_plot, y_gprR, color='darkorange', lw=lw,
         label='Right')
plt.plot(X_plot, y_gprL, color='blue', lw=lw,
         label='Left')
plt.xlabel('raw units')
plt.ylabel('[Newtons]')
plt.title('Left Hand: coef: %.4f   Right Hand: coef: %.4f' %(coefL, coefR))
plt.legend(loc="best",  scatterpoints=1)
plt.ylim(-1,10)
plt.xlim(-1,200)
plt.show()


#%%
from numpy import arange
from scipy.optimize import curve_fit
from matplotlib import pyplot

x=Xl.astype(np.float64).flatten()
y=yl.astype(np.float64).flatten()

def objective4(x, a, b, c, d):
	return a * x + b * x**2 + c * x**3 + d 
def objective3(x, a, b, c):
	return a * x + b * x**2 + c * x**3 #+ d 

popt, _ = curve_fit(objective4, x, y)
a, b, c, d = popt
print('y = %.5f * x + %.5f * x^2 + %.10f * x^3  + %.5f' % (a, b, c, d))
x_line4 = arange(min(x), 2500, 1)
y_line4 = objective4(x_line4, a, b, c, d)

# popt, _ = curve_fit(objective3, x, y)
# a, b, c = popt
# print('y = %.5f * x + %.5f * x^2 + %.10f * x^3 ' % (a, b, c))
# x_line3 = arange(min(x), 2500, 1)
# y_line3 = objective3(x_line3, a, b, c)

pyplot.scatter(x, y)
plt.plot(x_line4, y_line4, '--', color='red')
plt.plot(X_plot, y_gprL, color='blue', lw=lw,
         label='Left')
#plt.plot(x_line3, y_line3, '--', color='green')
plt.title('y = %.5f * x + %.5f * x^2 + %.5f * x^3  + %.5f' % (a, b, c, d))
plt.xlim(0,100)
plt.ylim(0,10)
plt.xlabel('raw units')
plt.ylabel('[Newtons]')
plt.show()



#%% 
coefs = [regL.coef_[0], regL.intercept_, regR.coef_[0], regR.intercept_]
np.save("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/calicoefs.npy", coefs)





#%%
from numpy import arange
from scipy.optimize import curve_fit
from matplotlib import pyplot

x=Xl.astype(np.float64).flatten()
y=yl.astype(np.float64).flatten()

def objective(x, a, b, c):
	return a * x + b * x**2 + c * x**3 #+ d 
popt, _ = curve_fit(objective, x, y)
a, b, c = popt
print('y = %.5f * x + %.5f * x^2 + %.10f * x^3 ' % (a, b, c))
x_line = arange(min(x), 2500, 1)
y_line = objective(x_line, a, b, c)
pyplot.scatter(x, y)
plt.plot(x_line, y_line, '--', color='green')
plt.title('y = %.5f * x + %.5f * x^2 + %.5f * x^3 ' % (a, b, c))
plt.xlim(0,100)
plt.ylim(0,10)
plt.xlabel('raw units')
plt.ylabel('[Newtons]')
plt.show()
