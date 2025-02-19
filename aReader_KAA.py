#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:40:44 2017

@author: stoffer 
"""
import serial
import threading
import numpy as np
import time
import scipy.interpolate as interp
import platform
import serial.tools.list_ports
import ctypes


#%%

# import struct
# version = struct.calcsize("P")*8 
# print(version)

# import ctypes 
# import time
# par = ctypes.windll.inpoutx64 #if python runs in 64 bit mode
# port=0xd010 #port number
# bit0 = 1 #sets bit0
# bit1= 1**2 #sets bit1
# offstate = 0 #reset all bits
# par.Out32(port,bit0+bit1) #sets bit0 and bit1
# time.sleep(1.0)
# par.Out32(offstate) #set all bits off



#%%



def readloop(port,obj):
    ser = serial.Serial(obj.port,115200,timeout=0.)
    debug=obj.debug
    ser.flushInput()
    ser.flushOutput()
    buf = b''
    nsamp=np.uint64(1)
    if not obj.dump is None:
        dump = open(obj.dump,'wb')
        np.float64(time.time()).tofile(dump)
        np.uint64(2).tofile(dump)
    obj.i = 0
    t0=time.time()
    try:
        while not obj.stopev.is_set():
            buf += ser.read(ser.inWaiting())
            lines = buf.split(b'\n')
            for line in lines[:-1]:
                try:
                    x = np.fromstring(line,dtype=np.int16,sep=' ')
                    t = np.float64(time.time())
                    if x.shape[0] == obj.cache.shape[1]:
                        obj.lock.acquire()
                        if obj.i >= obj.cache.shape[0]:
                            obj.i = 0
                        obj.cache[obj.i,:] = x
                        obj.i += 1        
                        obj.lock.release()
                        if not obj.dump is None:
                            t.tofile(dump)
                            nsamp.tofile(dump)
                            x.tofile(dump)
                except:
                    pass
                        
            buf=lines[-1]
            if debug and (time.time()-t0)>1:
                print('%s, %i'%(lines,ser.isOpen()))
                t0=time.time()
    finally:
        print('closing serial port')
        ser.close()
        if not obj.dump is None:
            dump.close()
    
   # os.chdir(path)

class aReader:
    def __init__(self,port=None,nchannels=2,dump=None,ncache=500*60*20,debug=False):
        if port is None:
            ports=[list(i) for i in serial.tools.list_ports.comports()]
            #print(ports)
            p=np.nonzero([i[1].find('CP210x')>0 for i in ports])[0]
            if len(p)>0:
                p=int(p[0])
                port=ports[p][0]
                print('Port identified %s'%port)
        self.port=port
        self.dump=dump
        self.debug=debug
        self.stopev = threading.Event()
        self.lock = threading.RLock()
        self.ncache = ncache
        self.cache = np.zeros((ncache,nchannels+1),dtype=np.int16)
        self.i = 0
        self.thread=threading.Thread(target=readloop,args=(port,self))
        self.thread.start()
        #self.calibration=np.load("C:/Users/dzn332/Documents/GitHub/BIMANUAL_KAA21/Calibration/calicoefs.npy")
    
    def getValues(self,hist=1):
        if hist>self.ncache:
            hist=self.ncache
        self.lock.acquire()
        wraparound=self.i-hist
        if wraparound<0:
            x=np.concatenate((self.cache[wraparound:],self.cache[:self.i]),axis=0).copy()
        else:
            x=self.cache[wraparound:self.i].copy()
        self.lock.release()
        # [Lcoef, Lint, Rcoef, Rint]=self.calibration
        # xnewt = Rint + Rcoef*x         
        return x
    
    # def getValues(self,hist=1):
    #     if hist>self.ncache:
    #         hist=self.ncache
    #     self.lock.acquire()
    #     wraparound=self.i-hist
    #     if wraparound<0:
    #         x=np.concatenate((self.cache[wraparound:],self.cache[:self.i]),axis=0).copy()
    #     else:
    #         x=self.cache[wraparound:self.i].copy()
    #     self.lock.release()
    #     x=self.calibration[x[:,1:]]
    #     return x
    
    def stop(self):
        self.stopev.set()
        self.thread.join(1.)
    
    def __del__(self):
        self.stop()
'''
#Example:
if __name__ == "__main__":
    import time
    a=aReader(port='/dev/ttyUSB0',nchannels=2,dump=None,ncache=1000)
    for i in range(1000):
        print(a.getValues(1))
        time.sleep(0.01)
        
'''