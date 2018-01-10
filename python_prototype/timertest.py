from tkinter import *
from tkinter import ttk

import threading
import time


class TimerFrame( Frame ):

    def __init__ ( self, parent ):
        Frame.__init__( self, parent )

        # Timer

        self.pom_minutes = 25
        self.pom_seconds = 0

        self.pom_time = StringVar()
        self._set_pom_time()

        Label( self, textvariable=self.pom_time, font=( 'Source Code Pro', 12 ) )\
            .grid( row=0, column=0, columnspan=3 )
            
        self.btn_start = Button( self, text='Start', command=self._start_pom )
        self.btn_start.grid( row=1, column=0, sticky=E+W )

        self.btn_stop = Button( self, text='Stop', command=self._stop_pom )
        self.btn_stop.grid( row=1, column=1, sticky=E+W )

        self.btn_reset = Button( self, text='Reset', command=self._reset_pom )
        self.btn_reset.grid( row=1, column=2, sticky=E+W )

        #Entry( self, textvariable=test ).grid( row=0, column=1 )

        self.timer = Timer( 25*60 )


    def _set_pom_time( self ):

        self.pom_time.set( "{:02d}:{:02d}".format(*divmod( self.pom_seconds, 60)) )

    def _start_pom( self ):
        self.timer.start()

    def _stop_pom( self ):
        self.timer.stop()

    def _reset_pom( self ):
        self._stop_pom()
        self.timer



class Timer( threading.Thread ):

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


if __name__ == '__main__':

    timer = Timer( 3 )
    timer.start()
