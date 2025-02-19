# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:08:32 2021
@author: dzn332
"""


# lav loop, hvert sekund skift, time.sleep , state 255 and 0 
import struct
import ctypes 
import time
version = struct.calcsize("P")*8
par = ctypes.windll.inpoutx64 #if python runs in 64 bit mode
port=0x3FF8 #port number
offstate = 0 
for i in range(0,5):
    #print(i)
    state=0
    par.Out32(port,state)
    print(par.Inp32(port))
    time.sleep(0.1)
    
    state=5
    par.Out32(port,state)
    print(par.Inp32(port))
    time.sleep(0.1)

state=0
par.Out32(port,state)
    
    
# pin out 
# pin0 = 1 - 8
# 37
# bit1 = pin1+pin37 



#%%
# # Send triggers to EEG system 
# state=0 
# time.sleep(1.0)

# import struct
# version = struct.calcsize("P")*8 
# #print(version) 
# import ctypes 
# import time
# par = ctypes.windll.inpoutx64 #if python runs in 64 bit mode
# port=0x3FF8 #port number
# bit0 = 1 #sets bit0
# bit1= 1**2 #sets bit1
# offstate = 0 #reset all bits
# par.Out32(port+2,0) # sets port in mode to send
# # ############## 
# par.Out32(port,255) #sets bit0 and bit1
# time.sleep(1.0)
# par.Out32(offstate) #set all bits off


# # restart com, tjek driver install 

