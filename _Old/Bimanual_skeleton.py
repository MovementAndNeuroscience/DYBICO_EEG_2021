from psychopy import visual ,event, gui, core
import numpy,datetime,scipy.io,os,time
import numpy as np
import aReader_fast as aReader

class CircleScene:
    def __init__(self,mywin):
        #Draw vars
        self.textcol=(1,1,1)
        self.targetcol=(0.5,0.5,-1)
        self.forcecol=(0.7,0.3,-1)
        self.mixcol=(0.6,0.4,-1)
        self.backcol=(0.,0.,.0)
        self.forceWidth=10
        self.targetWidth=3
        self.aspectrsc=float(mywin.size[0])/mywin.size[1]#scaling of the screen
        #Objects
        cres=50#defines visual feedback circle
        cR=.5
        p=-numpy.linspace(0,2*numpy.pi,cres)+numpy.pi/2
        cc=numpy.vstack(((0,0),cR*numpy.array((numpy.cos(p),numpy.sin(p))).T))
        p1=np.linspace(-.5*np.pi,.5*np.pi,256)
        halfc1=np.vstack((np.cos(p1),np.sin(p1))).T*np.array((1./self.aspectrsc,1))[None,:]
        halfc2=np.vstack((-np.cos(p1),np.sin(p1))).T*np.array((1./self.aspectrsc,1))[None,:]
        interp=True
        aspectrsc=float(mywin.size[0])/mywin.size[1]
        self.circ1= visual.ShapeStim(win=mywin, units='norm', lineWidth=10.0, lineColor='red', lineColorSpace='rgb', fillColor=None,\
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
    
    def draw(self, sizes=None, targets=None):
        self.circ1.setLineWidth(self.forceWidth)
        self.circ1.setColor(self.forcecol,'rgb')
        self.circ1.setSize((self.right,self.right))
        self.circ1.draw()
        self.circ2.setLineWidth(self.forceWidth)
        self.circ2.setColor(self.forcecol,'rgb')
        self.circ2.setSize((self.left,self.left))
        self.circ2.draw()
        self.lin1.setLineWidth(self.forceWidth)
        self.lin1.setColor(self.forcecol,'rgb')
        self.lin1.setSize((self.right,self.right))
        self.lin1.draw()
        self.lin2.setLineWidth(self.forceWidth)
        self.lin2.setColor(self.forcecol,'rgb')
        self.lin2.setSize((self.left,self.left))
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

if __name__=='__main__':
    
    
    mywin1 = visual.Window([512,512]) # create a window
    lognobox=gui.Dlg(title='Subject information')
    lognobox.addField('Logno:','')
    lognobox.addField('Max force:','800')
    lognobox.show()

    if gui.OK:
        logno=lognobox.data[0]
        maxforce=int(lognobox.data[1])
        print('log number: %s, maxforce: %i'%(logno,maxforce))
    else:
        print('user cancelled')
    mywin1.close()
    
    
    
    mywin=visual.Window(size=[800,600],fullscr=False,screen=0)
    mywin.setMouseVisible(False)
    scene=CircleScene(mywin)
    timestamp=time.time()
    timestamp_readable=datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H-%M-%S')
    filename='kaatest_bimanual_%s.raw'%timestamp_readable
    appleJack=aReader.aReader(debug=False,dump=filename)
    offset = np.array((1575,1575))[None]
    def readForce(scaling=maxforce):
        v=appleJack.getValues(5)[:,1:]-offset #read and correct offset
        v=v.mean(0)/scaling
        return v[0],v[1]
    
    stop = False
    
    baseline = (0.1, 0.1)
    targets = ((0.5, 0.5), (0.5, 0.25), (0.75, 0.5))
    N = 10
    conditions = np.random.permutation(np.arange(N) % 3) #three alternating conditions
    durations = 1.0 * np.ones(N) #6 seconds duration
    onsets = np.cumsum(3.0 + (np.random.rand(N)-0.5)*4) #10 secs +/- 2
    
    conditions = np.concatenate(((0,),conditions))
    durations = np.concatenate(((10,),durations))
    onsets = np.concatenate(((0,), 10+onsets))
    
    trial = 0
    globalClock = core.Clock()
    t0 = globalClock.getTime()
    
    while not stop:
        
        t = globalClock.getTime()-t0
        if trial<len(onsets)-1 and t>=onsets[trial+1]:
            trial += 1
        if trial<len(onsets) and t-onsets[trial]<durations[trial]:
            scene.targetLeft,scene.targetRight = targets[conditions[trial]]
        else:
            scene.targetLeft, scene.targetRight = baseline
        scene.right, scene.left = readForce()
        scene.draw()
        mywin.flip()
        
        keys=event.getKeys()
        if len(keys)>0:
            if keys[0] == 'q':
                stop = True
    appleJack.stop()
    del appleJack
    mywin.close()
    core.quit()