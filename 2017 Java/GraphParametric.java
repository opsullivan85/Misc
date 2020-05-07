import java.awt.*;
import java.util.*;

class GraphParametric{
      
      public static final int SIZE = 1000;
      public static final int QUALITY = 4;
      public static final Boolean GRIDLINES = true;
      public static final Boolean SLOWMOTION = false;
      
      public static void main(String[] args){
            DrawingPanel panel = new DrawingPanel(SIZE, SIZE);
            Graphics g = panel.getGraphics();
            
            double xt, yt;
            double xMin = -2;
            double xMax = 2;
            double yMin = -2;
            double yMax = 2;
            double xRange = xMax - xMin;
            double yRange = yMax - yMin;
            int width = 5;
            
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
            
            //For loop finds x & y given t, then graphs point
            for(double t = 0; t <= 2; t += 1.0/Math.pow(10,QUALITY)){
/*x(t) equation*/ xt = Math.pow(2*Math.sin(4*Math.PI*t),5);
/*y(t) equation*/ yt = Math.pow(2*Math.cos(3*Math.PI*t),5);
                  int h = (int)((xt*SIZE/xRange/32)-(width/2)-(xMin*SIZE/xRange));
                  int v = SIZE-(int)((yt*SIZE/yRange/32)+(width/2)-(yMin*SIZE/yRange));
                  g.fillOval(h,v,width,width);
                  if(SLOWMOTION){
                        panel.sleep(1);
                  }
            }

            
            System.out.println("Done!");
      }
}