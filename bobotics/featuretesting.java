package bobotics;

import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import java.awt.event.KeyAdapter;

public class featuretesting {

    static int button2X = 0;
    static boolean but2Xcheck = false;
    static int keyCode;
    static int pos = 10000;
    static double pos1 = 0;

    static int isClimbing = 0;
    static double wristpower = 0;
    static int isSliding = 0;
    static int buttonX = 0;

    static double kp = 1.1;
    static double ki;
    static double kd;
    static double error = 100;
    static double enc;
    static double targ = 1000;
    static double pwr;


    int buttonA =0;

    public static void main(String[] args) throws Exception {

        JFrame myJFrame = new JFrame();

        myJFrame.addKeyListener (new KeyAdapter() {
            
            public void keyPressed(KeyEvent e) {
                keyCode = e.getKeyCode();
            }
            
            public void keyReleased(KeyEvent e){
                keyCode = 0;
            }
            
        });
        myJFrame.setVisible(true);

        while (true){

            pwr = error*kp;
            System.out.println(pwr);

            /*
            if (keyCode == KeyEvent.VK_A && !but2Acheck) {
                button2A += 1;
                but2Acheck = true;
            }
            if (keyCode != KeyEvent.VK_A){
                but2Acheck = false;
            }
            if (!but2Acheck) {
                if (button2A % 2 == 1) {
                    if (pos > 0){
                        pos --;
                    } else {
                        //System.out.println(pos);
                    }
                } else {
                    if (pos < 1000){
                        pos ++;
                    } else {
                        //System.out.println(pos);
                    }
                }
            }
            */
        }
    }
}