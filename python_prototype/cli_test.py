import threading
import time


class Ticker( object ):

    def __init__( self, time=0 ):
        self.ticker = threading.Timer( 1, self._tick )
        self.time = time
        self.run = True

    def start( self ):
        self._tick()

    def get_time( self ):
        return self.time

    def stop( self ):
        self.run = False

    def _tick( self ):
        print( "TICK: ", self.time )
        if( self.run ):
            self.time += 1
            self.ticker = threading.Timer( 1, self._tick )
            self.ticker.start()


class Tocker( object ):

    def __init__( self, time ):
        self.tocker = threading.Timer( 1, self._tock )
        self.time = time

    def start( self ):
        self.tocker.start()
    
    def get_time( self ):
        return self.time

    def _tock( self ):
        print( "TOCK: ", self.time )
        if( self.time > 0 ):
            self.time -= 1
            self.tocker = threading.Timer( 1, self._tock )
            self.tocker.start()


if __name__=='__main__':

    stopwatch = Ticker()
    stopwatch.start()

    time.sleep( 10 )
    
    stopwatch.stop()

    timer = Tocker( stopwatch.get_time() // 3 )
    timer.start()