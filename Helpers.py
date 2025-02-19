# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 13:19:30 2021
@author: Keenie Ayla
HELPER FUNCTIONS 
"""

#%% ##########################################################################


#%% ##########################################################################
def trigger(trigger_state, send_trigger=True):
    #import struct
    import ctypes 
    import time
    #version = struct.calcsize("P")*8
    par = ctypes.windll.inpoutx64 #if python runs in 64 bit mode
    port=0x3FF8 #port number
    offstate = 0
    
    state=int(trigger_state)
    on_time=0.01
    global_time = time.time()
    while time.time()-global_time<on_time:
        par.Out32(port, state)
        #print(par.Inp32(port))
    par.Out32(port, offstate)
    print('Trigger being sent: %s'%state)
        

#%% ##########################################################################
def get_block(no_of_blocks, trial_repetitions, targets, jitter_time, trial_duration, baseline_between_trials, initial_dur, time_between_blocks):
    import numpy as np 
    blocks, onsets_blocked, durations_blocked=[],[],[]
    for j in range(no_of_blocks): 
        block = []
        for i in range(trial_repetitions): 
            block.append(np.arange(len(targets)-1)+1)
        block=np.concatenate(block)
        
        # First block starts with pause followed by baseline 
        block_p=np.insert(np.random.permutation(block), 0, (0,1)) # conditions [1:] are in randomized order
        blocks.append(block_p)
        
        # introducing jitter on both duration [+-sec] and onset [+sec]        
        jitter_durations_blocked = 2*jitter_time*(np.random.rand(len(block_p))-0.5)
        jitter_onsets_blocked = abs(2*jitter_time*(np.random.rand(len(block_p))-0.5))

        dur_blocked = (trial_duration + jitter_durations_blocked) * np.ones(len(block_p)) # seconds duration
        ons_blocked = dur_blocked + jitter_onsets_blocked + baseline_between_trials

        dur_blocked[0]=initial_dur
        dur_blocked[1]=initial_dur
        if j==0: ons_blocked[0]=0
        ons_blocked[1]=dur_blocked[0]
        ons_blocked[2]=dur_blocked[0]
        
        durations_blocked.append(dur_blocked)
        onsets_blocked.append(ons_blocked)
        if j>=1:
            # introduce time to seperate blocks
            durations_blocked[j][0] = time_between_blocks # the pause condition 
            onsets_blocked[j][1] += durations_blocked[j][0] # the baseline that follows
        
    onsets_blocked=np.cumsum(onsets_blocked)
    conditions = np.concatenate(blocks)
    durations = np.concatenate(durations_blocked)
    onsets = onsets_blocked 
    print(conditions)
    return (conditions, durations, onsets)


#%% ##########################################################################
def get_targets(tasks, LH, RH, percent_change_from_baseline, pause_target):
    # DEFINE CIRCLE GOAL/TARGET SIZES - DEPENDING ON CONDITIONS SELECTED
    targets = []
    targets_names = []
    
    incr = 1+percent_change_from_baseline # increasing size 
    decr = 1-percent_change_from_baseline # decreased size 
     
    targets.append(pause_target)
    targets_names.append('Pause_between_blocks')
    if tasks['Baseline_force'][0] == 'Y': 
        targets.append((LH,RH))
        targets_names.append('Baseline_force')
    if tasks['Left_increase_force'][0] == 'Y': 
        targets.append((LH*incr,RH))
        targets_names.append('Left_increase_force')
    if tasks['Left_decrease_force'][0] == 'Y': 
        targets.append((LH*decr,RH))
        targets_names.append('Left_decrease_force')  
    if tasks['Right_increase_force'][0] == 'Y': 
        targets.append((LH,RH*incr))
        targets_names.append('Right_increase_force')
    if tasks['Right_decrease_force'][0] == 'Y': 
        targets.append((LH,RH*decr))
        targets_names.append('Right_decrease_force')
    if tasks['Sym_increase_force'][0] == 'Y': 
        targets.append((LH*incr,RH*incr))
        targets_names.append('Sym_increase_force')
    if tasks['Sym_decrease_force'][0] == 'Y': 
        targets.append((LH*decr,RH*decr))
        targets_names.append('Sym_decrease_force')
    if tasks['Asym_L_increase_R_decrease'][0] == 'Y': 
        targets.append((LH*incr,RH*decr))
        targets_names.append('Asym_L_increase_R_decrease')
    if tasks['Asym_L_decrease_R_increase'][0] == 'Y': 
        targets.append((LH*decr,RH*incr))
        targets_names.append('Asym_L_decrease_R_increase')
    
    return (targets, targets_names)  


#%% ##########################################################################
class CircleScene:
    def __init__(self,mywin):
        import numpy,datetime,scipy.io,os,time
        import numpy as np
        from psychopy import visual
        #Draw vars
        self.textcol=(1,1,1)
        self.targetcol=(-1,-1,1) #(0.5,0.5,-1)
        self.forcecol=(0.7,0.3,-1)
        self.forcecol0=(0.,0.,.0)
        self.mixcol=(0.6,0.4,-1)
        self.backcol=(0.,0.,.0)
        self.forceWidth=10 # linewidth of circle
        self.targetWidth=5 # linewidth of circle
        self.aspectrsc=float(mywin.size[0])/mywin.size[1]#scaling of the screen
        #Objects
        cres=50#defines visual feedback circle, KAA: changes nothing?
        cR=.5
        p=-numpy.linspace(0,2*numpy.pi,cres)+numpy.pi/2
        cc=numpy.vstack(((0,0),cR*numpy.array((numpy.cos(p),numpy.sin(p))).T))
        p1=np.linspace(-.5*np.pi,.5*np.pi,256)
        halfc1=np.vstack((np.cos(p1),np.sin(p1))).T*np.array((1./self.aspectrsc,1))[None,:]
        halfc2=np.vstack((-np.cos(p1),np.sin(p1))).T*np.array((1./self.aspectrsc,1))[None,:]
        interp=True
        aspectrsc=float(mywin.size[0])/mywin.size[1]
        self.circ1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc1, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.lin1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc1[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.circ2= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc2, closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.lin2= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor=None, lineColorSpace='rgb', fillColor=None,\
                fillColorSpace='rgb', vertices=halfc2[[0,-1],:], closeShape=False, pos=(0, 0), ori=0.0, opacity=1.0,\
                interpolate=interp)
        self.fixation=visual.TextStim(mywin,text='+',color=(1,-1,-1),alignHoriz='center', alignVert='center')
        self.circle=visual.Circle(mywin,radius=(1./aspectrsc,1.),edges=512,lineColor=None,interpolate=False)
        self.circleline=visual.Circle(mywin,radius=(1./aspectrsc,1.),edges=512,lineColor=(0,0,0),interpolate=False,fillColor=None,lineWidth=3.)
        interp=False
        P1=.1*numpy.array(((-1, -1), (1, -1), (0, 1)))
        self.targetLeft=0.5
        self.targetRight=0.5
        self.left=0.5
        self.right=0.5
        
        self.txt=visual.TextStim(mywin,pos=(0,.9))
        
    
    def draw(self, sizes=None, targets=None):
        self.circ1.setLineWidth(self.forceWidth)
        self.circ1.setSize((self.right,self.right))
        self.lin1.setLineWidth(self.forceWidth)
        self.lin1.setSize((self.right,self.right))
        if self.right<0.15 :
            self.circ1.setColor(self.forcecol0,'rgb')
            self.lin1.setColor(self.forcecol0,'rgb')
        else : 
            self.circ1.setColor(self.forcecol,'rgb')
            self.lin1.setColor(self.forcecol,'rgb')
        self.circ1.draw()
        self.lin1.draw()

        self.circ2.setLineWidth(self.forceWidth)
        self.circ2.setSize((self.left,self.left))
        self.lin2.setLineWidth(self.forceWidth)
        self.lin2.setSize((self.left,self.left))
        if self.left<0.15 :
            self.circ2.setColor(self.forcecol0,'rgb')
            self.lin2.setColor(self.forcecol0,'rgb')
        else :
            self.circ2.setColor(self.forcecol,'rgb')
            self.lin2.setColor(self.forcecol,'rgb')
        self.circ2.draw()
        self.lin2.draw()
        
        self.circ1.setLineWidth(self.targetWidth)
        self.circ1.setColor(self.targetcol,'rgb')
        self.circ1.setSize((self.targetRight,self.targetRight))
        self.circ1.draw()
        self.circ2.setLineWidth(self.targetWidth)
        self.circ2.setColor(self.targetcol,'rgb')
        self.circ2.setSize((self.targetLeft,self.targetLeft))
        self.circ2.draw()
        self.lin1.setLineWidth(self.targetWidth)
        self.lin1.setColor(self.targetcol,'rgb')
        self.lin1.setSize((self.targetRight,self.targetRight))
        self.lin1.draw()
        self.lin2.setLineWidth(self.targetWidth)
        self.lin2.setColor(self.targetcol,'rgb')
        self.lin2.setSize((self.targetLeft,self.targetLeft))
        self.lin2.draw()
        
        if self.targetRight == 0.01 :
            self.txt.setText('Pause')
            self.txt.draw()

