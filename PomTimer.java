import java.util.Timer;
import java.util.TimerTask;

public class PomTimer {

    private int workSeconds;
    private Timer timer = new Timer();


    PomTimer() {
        workSeconds = 25*60;  // 25 Minutes
    }

    PomTimer( int seconds ) {
        workSeconds = seconds;
        System.out.println( "PomTimer created " );
    }
    
    public void start() {

        timer.scheduleAtFixedRate( new SecondTask(), 0, 1000 );
    }

    class SecondTask extends TimerTask {

        @Override
        public void run() {

            if( workSeconds == 0 ) {
                timer.cancel();
            }
            
            workSeconds--;
            System.out.println( Integer.toString(workSeconds/60) + ":" + Integer.toString(workSeconds%60) );
        }
    }

}