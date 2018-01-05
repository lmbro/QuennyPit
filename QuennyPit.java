import java.util.Timer;
import java.util.TimerTask;

public class QuennyPit {

    public static void main( String[] args ) {

        PomTimer pom = new PomTimer();
        PomTimer minute = new PomTimer( 60 );

        pom.start();
        minute.start();
    }
}