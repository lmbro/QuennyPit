import threading
import time

from tkinter import *
from tkinter import ttk
from tkinter.font import Font



class FiftyTwoSeventeen( Tk ):

    def __init__( self, parent ):
        Tk.__init__( self, parent )

        self.title( "Fifty-Two Seventeen" )

        Kesha( self ).pack( expand=TRUE, fill=BOTH )

class Kesha( Frame ):

    def __init__( self, parent ):
        Frame.__init__( self, parent )

        self.parent = parent

        # Clocks
        self.clock = Ticker( self )
        self.clock_net = Ticker( self, 0, 3 )
        self.clock_net_started = False

        # Buttons
        self.btn_work = Button( self, text='Work', command=self._start_work )
        self.btn_rest = Button( self, text='Rest', command=self._start_rest )
        #self.btn_reset = Button( self, text='RESET', command=self._reset_work_time )

        
        # Geometry
        self.clock.grid( row=0, column=0, columnspan=2, sticky=N+S+E+W )
        self.clock_net.grid( row=1, column=0, columnspan=2, sticky=N+S+E+W )
        
        self.btn_work.grid( row=2, column=0, sticky=N+S+E+W )
        self.btn_rest.grid( row=2, column=1, sticky=N+S+E+W )

        self.rowconfigure( 0, weight=1 )
        self.rowconfigure( 1, weight=1 )
        self.rowconfigure( 2, weight=1 )
        self.columnconfigure( 0, weight=1 )
        self.columnconfigure( 1, weight=1 )

    def stop_net( self ):
        self.clock_net.stop()
        self.clock_net = Ticker( self, self.clock_net.get_time(), 3 )
        self.clock_net.grid( row=1, column=0, columnspan=2, sticky=NSEW )
        self.clock_net_started = False
        return

    def reset_net( self ):
        self.clock_net.stop()
        self.clock_net = Ticker( self, 0, 3 )
        self.clock_net.grid( row=1, column=0, columnspan=2, sticky=NSEW )
        self.clock_net_started = False
        return

    def _start_work( self ):
        self.clock.stop()
        self.clock = Ticker( self )
        self.clock.grid( row=0, column=0, columnspan=2, sticky=N+S+E+W )
        self.clock.start()
        if( not self.clock_net_started ):
            self.clock_net.start()
            self.clock_net_started = True
        return

    def _start_rest( self ):
        self.clock.stop()
        self.clock = Tocker( self, self.clock.get_time() // 3 )
        self.clock.grid( row=0, column=0, columnspan=2, sticky=N+S+E+W )
        self.clock.start()
        return


class TickTock( Frame ):

    def __init__( self, parent, time=0, scaledown=1 ):
        Frame.__init__( self, parent )

        self.parent = parent
        self.time = time
        self.scaledown = scaledown
        self.run = True

        self.time_str = StringVar()
        self._format_time()
        self.font = Font( family="Source Code Pro" )
        
        Label( self, textvariable=self.time_str, font=self.font ).pack()

        self.bind( '<Configure>', self._resize )

    def get_time( self ):

        return self.time

    def _format_time( self ):
        self.time_str.set( "{:02d}:{:02d}".format(*divmod( self.time, 60)) )
        return

    def _resize( self, event ):
        height = ( self.winfo_width() ) // (-4*self.scaledown)
        print( height )
        self.font.configure( size=height )
        return


class Ticker( TickTock ):

    def __init__( self, parent, time=0, scaledown=1 ):
        TickTock.__init__( self, parent, time, scaledown )

        # Core operation
        self.ticker = threading.Timer( 1, self._tick )

    def start( self ):
        self._tick()

    def stop( self ):
        self.run = False

    def _tick( self ):
        self._format_time()
        if( self.run ):
            self.time += 1
            self.ticker = threading.Timer( 1, self._tick )
            self.ticker.start()


class Tocker( TickTock ):

    def __init__( self, parent, time=0, scaledown=1 ):
        TickTock.__init__( self, parent, time, scaledown )

        # Core operation
        self.tocker = threading.Timer( 1, self._tock )

    def start( self ):
        self._tock()

    def stop( self ):
        self.run = False
    
    def _tock( self ):
        self._format_time()
        if( (self.time > 0) and (self.run) ):
            self.time -= 1
            self.tocker = threading.Timer( 1, self._tock )
            self.tocker.start()
        elif( self.time <= 0 ):
            self.parent.stop_net()


if( __name__=='__main__' ):

    app = FiftyTwoSeventeen( None )
    app.mainloop()