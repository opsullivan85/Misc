import java.awt.*;

public class JavaBook {
      public static void main(String[] args){
            
            DrawingPanel panel = new DrawingPanel(800, 800);
            panel.setBackground(Color.WHITE);
            
            Graphics g = panel.getGraphics();
      
            draw(400, panel, 80, g, 0, 0);
            //draw(15, panel, 15, g, 220, 10);
            //draw(10, panel, 10, g, 380, 10);
      }
      
      public static void draw(int stairs, DrawingPanel panel, int size, Graphics g, int x, int  y){
            
            g.setColor(Color.CYAN);
            
            g.fillRect(x, y, 10*size, 10*size);
            
            Color brown = new Color(191, 118, 73);
            g.setColor(brown);
            
            for(int row = 1; row <= stairs; row++){
                  g.fillRect(x, 10*((y-size)+size*row)/stairs, 10*(size*row)/stairs, 10*(size-1)/stairs);
                  panel.sleep(stairs-row);
            }
            
            g.setColor(Color.WHITE);
            
            g.drawString("BJP", 5*size+x, 2*size+y);
            
      }
}