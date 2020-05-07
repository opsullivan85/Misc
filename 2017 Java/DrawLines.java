
import java.awt.*;
import java.util.*;

public class DrawLines{
      
      public static final int SIZE = 10000;
      public static final int INCREMENT = 25;
      
      public static void main(String[] args){
            
            DrawingPanel panel = new DrawingPanel(SIZE, SIZE);
            Graphics g = panel.getGraphics();
            Scanner console = new Scanner(System.in);
            Random rand = new Random();
            
            for(int i = 0; i < SIZE; i += INCREMENT){
                  g.drawLine(SIZE, SIZE, 0, SIZE-i);
                  panel.sleep(2);
                  g.drawLine(0, SIZE, i, 0);
                  panel.sleep(2);
                  g.drawLine(0, 0, SIZE, i);
                  panel.sleep(2);
                  g.drawLine(SIZE, 0, SIZE-i, SIZE);
                  panel.sleep(2);
            }
            
            for(int i = 0; i < SIZE; i += INCREMENT){
                  g.drawLine(SIZE, SIZE, i, 0);
                  panel.sleep(2);
                  g.drawLine(0, SIZE, SIZE, i);
                  panel.sleep(2);
                  g.drawLine(0, 0, SIZE-i, SIZE);
                  panel.sleep(2);
                  g.drawLine(SIZE, 0, 0, SIZE-i);
                  panel.sleep(2);
            }
            
            System.out.println("Done!");
      }
}
