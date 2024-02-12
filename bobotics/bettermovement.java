package bobotics;

import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import java.awt.event.KeyAdapter;

public class bettermovement {

    static int keyCode;

    static int button2X = 0;
    static boolean but2Xcheck = false;
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

    static int joy1x = 0;
    static int joy2x = 0;
    static int joy1y = 0;
    static int joy2y = 0;

    static double offset;
    static double FL;
    static double BL;
    static double FR;
    static double BR;

    public static void main(String[] args) throws Exception {

        JFrame myJFrame = new JFrame();

        myJFrame.addKeyListener (new KeyAdapter() {
            
            public void keyPressed(KeyEvent e) {
                keyCode = e.getKeyCode();
                System.out.println(keyCode);
            }
            
            public void keyReleased(KeyEvent e){
                keyCode = 0;
            }            
        });

        myJFrame.setVisible(true);
        
        // code to copy
        while (true){

            if (keyCode == 87){
                joy1y = 1;
            } else if (keyCode == 65){
                joy1x = 1;
            } else if (keyCode == 83){
                joy1y = -1;
            } else if (keyCode == 68){
                joy1x = -1;
            } else if (keyCode != 87 && keyCode != 65 && keyCode != 83 && keyCode != 68){
                joy1x = 0;
                joy1y = 0;
            }
            
            if (keyCode == 73){
                joy2y = 1;
            } else if (keyCode == 74){
                joy2x = 1;
            } else if (keyCode == 75){
                joy2y = -1;
            } else if (keyCode == 76){
                joy2x = -1;
            } else if (keyCode != 73 && keyCode != 74 && keyCode != 75 && keyCode != 76){
                joy2x = 0;
                joy2y = 0;
            }

            offset += joy2x;
            FL = (joy1y - joy1x - joy2x)/-offset;
            BL = (joy1y + joy1x - joy2x)/offset;
            FR = (joy1y + joy1x + joy2x)/offset;
            BR = (joy1y - joy1x + joy2x)/-offset;

            System.out.println(FL);
            System.out.println(FR);
            System.out.println(BL);
            System.out.println(BR);


//            System.out.println(joy1x);
//            System.out.println(joy1y);
//            System.out.println(joy2x);
//            System.out.println(joy2y);

            /*
            // toggle
            if (keyCode == KeyEvent.VK_A && !but2Acheck) {
                button2A += 1;
                but2Acheck = true;
            }
            if (keyCode != KeyEvent.VK_A){
                but2Acheck = false;
            }
            if (!but2Acheck) {
                if (button2A % 2 == 1) {
                    //System.out.println(pos);
                } else {
                    //System.out.println(pos);
                }
            }

            // run to position
            if (pos > 0){
                pos --;
            }
            */
        }
    }       
}
