import threading
import time

from tkinter import *
from tkinter import ttk


class FiftyTwoSeventeen( Tk ):

    def __init__( self, parent ):
        Tk.__init__( self, parent )

        self.parent = parent
        self.title( "Fifty-Two Seventeen" )

        self.clock = Ticker( self )
        self.clock.grid( row=0, column=0, columnspan=2 )

        self.btn_work = Button( self, text='Work', command=self._start_work )
        self.btn_work.grid( row=1, column=0, sticky=E+W )

        self.btn_rest = Button( self, text='Rest', command=self._start_rest )
        self.btn_rest.grid( row=1, column=1, sticky=E+W )

    def _start_work( self ):
        self.clock.stop()
        self.clock = Ticker( self )
        self.clock.grid( row=0, column=0, columnspan=2 )
        self.clock.start()

    def _start_rest( self ):
        self.clock.stop()
        self.clock = Tocker( self, self.clock.get_time() // 3 )
        self.clock.grid( row=0, column=0, columnspan=2 )
        self.clock.start()


class Ticker( Frame ):

    def __init__( self, parent, time=0 ):
        Frame.__init__( self, parent )

        # Core operation
        self.ticker = threading.Timer( 1, self._tick )
        self.time = time
        self.run = True

        # GUI Elements
        self.time_str = StringVar()
        self._format_time()
        Label( self, textvariable=self.time_str ).pack()

    def start( self ):
        self._tick()

    def stop( self ):
        self.run = False

    def get_time( self ):
        return self.time

    def _tick( self ):
        self._format_time()
        if( self.run ):
            self.time += 1
            self.ticker = threading.Timer( 1, self._tick )
            self.ticker.start()

    def _format_time( self ):
        self.time_str.set( "{:02d}:{:02d}".format(*divmod( self.time, 60)) )


class Tocker( Frame ):

    def __init__( self, parent, time ):
        Frame.__init__( self, parent )

        # Core operation
        self.tocker = threading.Timer( 1, self._tock )
        self.time = time
        self.run = True

        # GUI Elements
        self.time_str = StringVar()
        self._format_time()
        Label( self, textvariable=self.time_str ).pack()

    def start( self ):
        self._tock()

    def stop( self ):
        self.run = False
    
    def get_time( self ):
        return self.time

    def _tock( self ):
        self._format_time()
        if( (self.time > 0) and (self.run) ):
            self.time -= 1
            self.tocker = threading.Timer( 1, self._tock )
            self.tocker.start()

    def _format_time( self ):
        self.time_str.set( "{:02d}:{:02d}".format(*divmod( self.time, 60)) )


def tickTockTest():

    stopwatch = Ticker()
    stopwatch.start()

    time.sleep( 10 )
    
    stopwatch.stop()

    timer = Tocker( stopwatch.get_time() // 3 )
    timer.start()


if( __name__=='__main__' ):

    app = FiftyTwoSeventeen( None )
    app.mainloop()