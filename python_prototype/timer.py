from tkinter import *
from tkinter import ttk

import threading
import time

class Timer( Frame ):

    def __init__( self, parent, pom_duration=25*60 ):
        Frame.__init__( self, parent )

        self.parent = parent

        self.pom_duration = pom_duration
        self.seconds = [pom_duration]

        self.timer_strvar = StringVar()
        self._display_time()

        Label( self, textvariable=self.pom_time, font=( 'Source Code Pro', 12 ) )\
            .grid( row=0, column=0, columnspan=3 )

        self.btn_start = Button( self, text='Start', command=self._start_pom )
        self.btn_start.grid( row=1, column=0, sticky=E+W )

        self.btn_stop = Button( self, text='Stop', command=self._stop_pom )
        self.btn_stop.grid( row=1, column=1, sticky=E+W )
        self.btn_stop.confg( state=DISABLED )

        self.btn_reset = Button( self, text='Reset', command=self._reset_pom )
        self.btn_reset.grid( row=1, column=2, sticky=E+W )
        self.btn_reset.config( state=DISABLED )

    
    def _display_time():
        

    def _start_pom():

        self.btn_start.config( state=DISABLED )

        self.timer = 

        self.btn_stop.config( state=NORMAL )
        self.btn_reset.config( state=NORMAL )


    def _stop_pom():



    def _reset_pom():


    
class TimerThread( threading.Thread ):

    def __init__( self, seconds ):

        threading.Thread.__init__( self )
        self.event = threading.Event()
        self.seconds = seconds


    def run( self ):

        while( self.seconds > 0 and not self.event.is_set() ):
            print( self.seconds )
            self.seconds -= 1
            self.event.wait(1)


    def stop( self ):

        self.event.set()

    def set_time( seconds ):
        self.seconds = seconds