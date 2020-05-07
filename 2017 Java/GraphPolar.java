import java.awt.*;
import java.util.*;

class GraphPolar{
      
      public static final int SIZE = 1000;
      public static final int QUALITY = 4;
      public static final Boolean GRIDLINES = true;
      public static final Boolean SLOWMOTION = false;
      
      public static void main(String[] args){
            DrawingPanel panel = new DrawingPanel(SIZE, SIZE);
            Graphics g = panel.getGraphics();
            
            double equation;
            double size = 3;
            int width = 10;
            int shiftX = 0;
            int shiftY = 0;
            
            //Draws grid lines
            if(GRIDLINES){
                  Color grey = new Color(0.8f, 0.8f, 0.8f, 1f);
                  g.setColor(grey);
                  for(int i = 0; i <= width; i++)
                        g.drawLine(0,(int)(i*SIZE/width),SIZE,(int)(i*SIZE/width));
                  
                  for(int i = 0; i <= width; i++)
                        g.drawLine((int)(i*SIZE/width),0,(int)(i*SIZE/width),SIZE);
                  g.setColor(Color.BLACK);
                  g.drawLine(0,SIZE/2,SIZE,SIZE/2);
                  g.drawLine(SIZE/2,0,SIZE/2,SIZE);
            }
            
            //Finds distance as a function of the angle, and plots it
            for(double a = 0; a <= 2*Math.PI; a += 1.0/Math.pow(10,QUALITY)){
                  equation = 6*Math.sin(Math.cos(Math.sin(2*a)))-3.75;                    //Plug in equation here
                  dagSxSyw(equation*(SIZE/size),-a,g,shiftX,shiftY,size,width);
                  if(SLOWMOTION){
                        panel.sleep(1);
                  }
            }
            
            System.out.println("Done!");
      }
      
      //Method which plots a point given an angle, distance, a x and y shift, the drawingpanel size, and the point width
      public static void dagSxSyw(double d, double a, Graphics g, int shiftX, int shiftY, double size, int width){
            g.fillOval((int)(SIZE/2+d*Math.cos(a)+shiftX*(SIZE/size)-width/2),(int)(SIZE/2+d*Math.sin(a)-shiftY*(SIZE/size)-width/2),width,width);
      }
}