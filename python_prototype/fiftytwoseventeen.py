import threading
import time

from tkinter import *
from tkinter import ttk
from tkinter.font import Font


class FiftyTwoSeventeen( Tk ):

    def __init__( self, parent ):
        Tk.__init__( self, parent )

        self.parent = parent
        self.title( "Fifty-Two Seventeen" )

        # Master Frame
        self.master_frame = Frame( self )

        # Clock
        self.clock = Ticker( self.master_frame )

        # Buttons
        self.btn_work = Button( self.master_frame, text='Work', command=self._start_work )
        self.btn_rest = Button( self.master_frame, text='Rest', command=self._start_rest )

        # Geometry

        self.master_frame.pack( expand=TRUE, fill=BOTH )
        
        self.clock.grid( row=0, column=0, columnspan=2, sticky=N+S+E+W )
        self.btn_work.grid( row=1, column=0, sticky=E+W )
        self.btn_rest.grid( row=1, column=1, sticky=E+W )

        self.master_frame.rowconfigure( 0, weight=1 )
        self.master_frame.rowconfigure( 1, weight=1 )
        self.master_frame.columnconfigure( 0, weight=1 )
        self.master_frame.columnconfigure( 1, weight=1 )


    def _start_work( self ):
        self.clock.stop()
        self.clock = Ticker( self.master_frame )
        self.clock.grid( row=0, column=0, columnspan=2, sticky=N+S+E+W )
        self.clock.start()
        return

    def _start_rest( self ):
        self.clock.stop()
        self.clock = Tocker( self.master_frame, self.clock.get_time() // 3 )
        self.clock.grid( row=0, column=0, columnspan=2, sticky=N+S+E+W )
        self.clock.start()
        return


class Ticker( Frame ):

    def __init__( self, parent, time=0 ):
        Frame.__init__( self, parent )

        # Core operation
        self.ticker = threading.Timer( 1, self._tick )
        self.time = time
        self.run = True

        # GUI Elements
        self.time_str = StringVar()
        self.font = Font( family="Source Code Pro", size=20 )
        self._format_time()
        Label( self, textvariable=self.time_str, font=self.font ).pack()

        self.bind( '<Configure>', self._resize )

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

    def _resize( self, event ):
        height = ( self.winfo_width() ) // -4
        print( height )
        self.font.configure( size=height )


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