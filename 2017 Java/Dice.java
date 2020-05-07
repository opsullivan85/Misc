import java.util.*;
import java.io.*;

class dice{
      public static void main(String[] args){
            Random rand = new Random();
            int trials = 100;
            int samples = 100;
            int max = 80;
            long t0, t1, tt0, tt1;
            
            try {
                  //Create file
                  File file = new File("Dice.csv");
                  file.createNewFile();
                  PrintWriter printWriter = new PrintWriter(file);
                  
                  //Output header
                  ////System.out.printf("Streak without 7: %d trial(s), and %d sample(s) with a maximum of %d.\n", trials, samples, max);
                  printWriter.printf("Streak without 7: %d trial(s), and %d sample(s) with a maximum of %d.\n", trials, samples, max);
                  
                  //Output first row
                  for(int i = 1; i <= max; i++){
                        //System.out.printf("%4d,",i);
                        printWriter.printf("%4d,",i);
                  }
                  //System.out.println(" Trial total time");
                  printWriter.println(" Trial total time");
                  
                  //Output data rows
                  while(trials > 0){
                        System.out.println(101-trials);
                        tt0 = System.currentTimeMillis();
                        for(int i = 1; i <= max; i++){
                              t0 = System.currentTimeMillis();
                              for(int h = samples; h > 0; h--){
                                    roll(i, rand);
                              }
                              t1 = System.currentTimeMillis();
                              //System.out.printf("%5d,",t1-t0);
                              printWriter.printf("%5d,",t1-t0);
                        }
                        tt1 = System.currentTimeMillis();
                        //System.out.println(" " + (tt1-tt0));
                        printWriter.println(" " + (tt1-tt0));
                        trials--;
                  }
                  
                  //Close file
                  printWriter.flush();
                  printWriter.close();
            } catch (IOException e) {
                  e.printStackTrace();
            }
            
            System.out.print("Done!");
      }
      
      //Method to get a streak without rolling a sum of 7
      public static void roll(int streak, Random rand){
            int count = 0;
            while(count < streak){
                  if(rand.nextInt(7) + rand.nextInt(7) != 7)
                        count++;
                  else
                        count = 0;
            }
      }
}