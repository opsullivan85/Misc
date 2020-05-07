import java.awt.*;

public class Mandelbrot{
      
      public static int WIN_SIZE = 1000;
      public static double ZOOM = 1;
      public static double REAL = 0;
      public static double IMAG = 0;
      public static int MAX_ITER = 1000;
      
      public static void main(String[] args){
            drawMandelbrot(100, -0.25, 0, 2550);
      }
      
      public static void drawMandelbrot(double zoom, double real, double imag, int maxIter){
            int width = 100, height = 100;
            double Xmin = -2.0/zoom+real, Xmax = 2.0/zoom+real, Ymin = -2.0/zoom+imag, Ymax =2.0/zoom+imag;
            /*
             * 1(0,0) -> [(-2,-2), (2,2)]
             * 2(0,0) -> [(-1,-1), (1,1)]
             * 4(0,0) -> [(-0.5,-0.5), (0.5,0.5)]
             * 1(1,1) -> [(-1,-1), (3,3)]
             * 2(1,1) -> [(0,0), (2,2)]
             * 4(1,1) -> [(-0.5,-0.5), (0.5,0.5)]
             */
            StdDraw.setCanvasSize(width,height);
            StdDraw.setXscale(Xmin,Xmax);
            StdDraw.setYscale(Ymin,Ymax);
            StdDraw.setPenRadius(0);
            StdDraw.setPenColor(50, 50, 50);
            StdDraw.enableDoubleBuffering();
            Complex coord = new Complex(0, 0);
            Complex fx = new Complex(0, 0);
            int iteration = 0;
            int c = 0;
            int progress = 1;
            for(double a = Xmin; a <= Xmax; a += (Xmax-Xmin)/width){
                  for(double b = Ymin; b <= Ymax; b += (Ymax-Ymin)/height){
                        coord.setCoords(a,b);
                        fx.setCoords(a,b);
                        iteration = 1;
                        while(iteration < maxIter && fx.abs() < 2){
                              fx.squared();
                              fx.minus(coord);
                              iteration++;
                        }
                        
                        if(fx.abs() < 2){
                              StdDraw.setPenColor();
                              //StdDraw.setPenColor(255, 255, 255);
                              StdDraw.point(a, b);
                        } else{
                              c = (int)(255.0*(Math.log(iteration)/Math.log(maxIter)));
                              //StdDraw.setPenColor(0, 0, c);
                              StdDraw.setPenColor(255-c, 255-c, 255);
                              StdDraw.point(a, b);
                        }
                        
                  }
                  ///*
                  if((int)(100.0*((a-Xmin)/(double)(Xmax-Xmin)))+1 > progress){
                        progress = (int)(100.0*((a-Xmin)/(double)(Xmax-Xmin)))+1;
                        System.out.println(progress + "% Complete");
                  }
                  //*/
                  //System.out.println(a);
            }
            System.out.println("Processing Image");
            StdDraw.show();
            System.out.println("Done");
            
      }
}
class Complex{
      double real, imag;
      
      public Complex(double real, double imag){
            this.real = real;
            this.imag = imag;
      }
      
      public void setCoords(double real, double imag){
            this.real = real;
            this.imag = imag;
      }
      
      public void print(){
            System.out.println(this.real + " + " + this.imag + "i");
      }
      
      public void plus(int num){
            this.real += num;
      }
      
      public void plus(Complex num){
            this.real += num.real;
            this.imag += num.imag;
      }
      
      public void minus(int num){
            this.real -= num;
      }
      
      public void minus(Complex num){
            this.real -= num.real;
            this.imag -= num.imag;
      }

      public void times(int num){
            this.real *= num;
            this.imag *= num;
      }
      
      public void times(Complex num){
            double thisReal = this.real;
            double numReal = this.real;
            this.real = (this.real * num.real) - (this.imag * num.imag);
            this.imag = (this.imag * numReal) + (num.imag * thisReal);
      }
      
      public void squared(){
            double thisReal = this.real;
            this.real = (this.real * this.real) - (this.imag * this.imag);
            this.imag = (this.imag * thisReal) + (this.imag * thisReal);
      }
      
      public double abs(){
            return(Math.sqrt(this.real * this.real + this.imag * this.imag));
      }
}