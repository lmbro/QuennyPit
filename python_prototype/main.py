from tkinter import *
from tkinter import ttk

from timertest import *


class QuennyPit( Tk ):
    
    def __init__( self, parent ):
        Tk.__init__( self, parent )

        self.parent = parent
        self.title( "Quenny Pit" )

        TimerFrame( self ).grid( row=0, column=0 )


if __name__ == '__main__':

    app = QuennyPit(None )
    app.mainloop()