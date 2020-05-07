
import java.awt.*;
import java.util.*;

public class DrawCircles{
      
      public static final int SIZE = 10000;
      public static final int INCREMENT = 10;
      
      public static void main(String[] args){
            
            DrawingPanel panel = new DrawingPanel(SIZE, SIZE);
            Graphics g = panel.getGraphics();
            Scanner console = new Scanner(System.in);
            Random rand = new Random();
            
            //SIZE*Math.sqrt(2)+2000
            
            //3415
            //34142
            
            for(int i = 0; i < 5000; i += 10){
                  circle(i,i,i,g);
                  //panel.sleep(2);
                  circle(i,SIZE-i,i,g);
                  //panel.sleep(2);
                  circle(SIZE-i,i,i,g);
                  //panel.sleep(2);
                  circle(SIZE-i,SIZE-i,i,g);
                  //panel.sleep(2);
            }
            
            System.out.println("Done!");
      }
      public static void circle(int x, int y, int r, Graphics g){
            g.drawOval(x-r,y-r,2*r,2*r);
      }
}
