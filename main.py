from tkinter import *
import time
import pickle
from datetime import datetime

class StopWatch(Frame):                                                               
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self._isPause = False
        self._pausedTime = 0.0
        self._pauseStartTime = 0.0
        self.timestr = StringVar()               
        self.makeWidgets()      

    def makeWidgets(self): #time label                        
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.grid(row=0)
    
    def _update(self):  #-->Pause function
        if not self._isPause:
            self._elapsedtime = time.time() - self._pausedTime - self._start
            self._setTime(self._elapsedtime)
            self._timer = self.after(50, self._update)
            self._pauseStartTime = time.time()
        else:
            self._pausedTime = time.time() - self._pauseStartTime
    
     
    def _setTime(self, elap):  #setting time to hh:mm:ss
        hours = int(elap/60/60)
        if hours >= 1:
            minutes = int(elap/60 - hours*60.0)
            seconds = int(elap - 3600*hours - (minutes * 60))
        else:
            minutes = int(elap/60)
            seconds = int(elap - minutes*60.0)
        #mseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (hours, minutes, seconds))
        
    def Start(self):     #--> Start function                                                    
        if not self._running:
            self._isPause = False
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):    #-->stop function                                   
        if self._running:
            self._isPause = True
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0
            self._update()
                
    def Reset(self):       #-->Reset function                           
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
        
        
def main():
    root = Tk()
    root.title("StopWatch")
    sw = StopWatch(root)
    sw.grid(row=0, columnspan=4)

    Button(root, text='Start', command=sw.Start).grid(row=1, column=0)
    Button(root, text='Pause', command=sw.Stop).grid(row=1, column=1)
    Button(root, text='Reset', command=sw.Reset).grid(row=1, column=2)
    Button(root, text='Quit', command=root.quit).grid(row=1, column=3)
    
    root.mainloop()

if __name__ == '__main__':
    main()