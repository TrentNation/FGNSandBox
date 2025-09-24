import java.awt.Robot;            //Robot Class
import java.awt.event.InputEvent; //Mouse Events
import java.awt.event.KeyEvent;   //Keyboard Events
import java.awt.AWTEvent;         //Abstract Window Toolkit Events

public class AutoClicker {
    public static void main(String[] args) {
        /*
         * CheckList:
         * - [x] Import the necessary classes
         * - [x] Create the main method
         * - [x] Mouse Click Method
         * - [x] Key Click Method
         * - [ ] Add Stop Functionality
         * - [ ] Add GUI
         * - [ ] Add Settings
         */


        
        //Opening Line
        System.out.println("AutoClicker is running...");
        //End of Opening Line
        
        wait(5000);
        do{
            //System.out.println(java.awt.event.KeyEvent.getExtendedKeyCode());
            
            wait(5000); // 1000 ms = 1 second
            //mouseClick();
            //keyClick('A');
            //wait(750);
            //keyClick('B');a
            //mouseClick();

        }while(true);
        //End of Main Method

        //Closing Line
        // System.out.println("AutoClicker has finished clicking.");
        //End of Closing Line

    }
        public static void wait(int x) { //sleeps for 'x' amount of ms
        try {
            Thread.sleep(x); //Puts to Sleep
        } catch (InterruptedException e) { //Catches the error
            e.printStackTrace();
        }
    }
    //Mouse Click Method
        public static void mouseClick(){
           try {
            Robot bot = new Robot();
            bot.mousePress(InputEvent.BUTTON1_DOWN_MASK);    //Left Click Input
            bot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);  //Left Click Release
           } catch (Exception e) {
            e.printStackTrace();
           }
        }
        public static void keyClick(char key){
            try { Robot bot = new Robot();
                int keyCode = java.awt.event.KeyEvent.getExtendedKeyCodeForChar(key);
                // System.out.println("Key Code: " + keyCode); //Debugging Output
                bot.keyPress(keyCode); //Key Press Input
                bot.keyRelease(keyCode); //Key Release Input
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
