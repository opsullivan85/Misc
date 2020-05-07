import java.awt.*;
import java.util.*;

class GraphFunction{
      
      public static final int SIZE = 1000;
      public static final double QUALITY = 2;
      public static final Boolean GRIDLINES = true;
      public static final Boolean SLOWMOTION = false;
      
      public static void main(String[] args){
            DrawingPanel panel = new DrawingPanel(SIZE, SIZE);
            Graphics g = panel.getGraphics();
            
            double equation;
            double xMin = -10;
            double xMax = 10;
            double yMin = -10;
            double yMax = 10;

            int width = 5;
            double xRange = xMax - xMin;
            double yRange = yMax - yMin;
            
            //Draws grid lines
            if(GRIDLINES){
                  Color grey = new Color(0.8f, 0.8f, 0.8f, 1f);
                  g.setColor(grey);
                  for(double i = -(int)yRange; i <= yRange; i++) //-
                        g.drawLine(0,(int)((yMax+i)*SIZE/yRange),SIZE,(int)((yMax+i)*SIZE/yRange));
                  
                  for(int i = -(int)xRange; i <= xRange; i++)//|
                        g.drawLine((int)((-xMin+i)*SIZE/xRange),0,(int)((-xMin+i)*SIZE/xRange),SIZE);
                  g.setColor(Color.BLACK);
                  g.drawLine(0,(int)(yMax*SIZE/yRange),SIZE,(int)(yMax*SIZE/yRange));
                  g.drawLine((int)(-xMin*SIZE/xRange),0,(int)(-xMin*SIZE/xRange),SIZE);
            }
            
            //x*x+Math.sin(3*x); 
            //-0.1*x*x*x*x*x*x*x+1.6*x*x*x*x*x-6.2*x*x*x+4.3*x;    
            
            for(double x = xMin*1.25; x <= xMax*1.25; x += (xRange/SIZE)/Math.pow(10,QUALITY)){
                  equation = -0.1*x*x*x*x*x*x*x+1.6*x*x*x*x*x-6.2*x*x*x+4.3*x;                                         //Put equation here;;
                  int h = (int)(x*SIZE/xRange-width/2-(xMin*SIZE/xRange));
                  int v = SIZE-(int)(equation*SIZE/yRange+width/2-yMin*SIZE/yRange);
                  g.fillOval(h,v,width,width);
                  if(SLOWMOTION){
                        panel.sleep(1);
                  }
            }
            
            System.out.println("Done!");
      }
}