import java.util.*;

class PrintTimeMethod{
      public static void main(String[] args){
            
            long t0 = System.currentTimeMillis();           //start timer
            
            for(double i = 0; i <= 1000000000; i++){
            }
            
            long t1 = System.currentTimeMillis();           //stop timer
            
            time(t1 - t0);                                  //print elapsed time
      }
      
      public static void time(long t){
            
            int h = (((int)(t)/1000)/60)/60;
            int m = (((int)(t)/1000)/60)%60;
            int s = ((int)(t)/1000)%60;
            int ms = (int)(t)%1000;
            
            System.out.printf("%d hours %d minutes %d seconds and %d milliseconds.\n", h, m, s, ms);
      }
}
            