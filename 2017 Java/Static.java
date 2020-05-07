
import java.awt.*;
import java.util.*;

public class Static{
      
      public static void main(String[] args){
            
            DrawingPanel panel = new DrawingPanel(900, 900);
            Graphics g = panel.getGraphics();
            Scanner console = new Scanner(System.in);
            Random rand = new Random();
            Color grey = new Color(0f, 0f, 0f, 0.002f);
            g.setColor(grey);
            int count = 0;
            String reRun = "y";
            while(count<1000*1000*4){
                  //g.drawRect(rand.nextInt(1001),rand.nextInt(1001),1,1);
                  g.drawRect((int)((rand.nextDouble()*30)*(rand.nextDouble()*30)),
                             (int)((rand.nextDouble()*30)*(rand.nextDouble()*30)),1,1);
                  count++;
            }
            System.out.print("Re-Run?");
            reRun = console.next();
      }
}
