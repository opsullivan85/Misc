import java.util.*;

class Weather{
      public static void main(String[] args){
            Scanner console = new Scanner(System.in);
            
            System.out.print("How many days' temperatures? ");
            
            int[] temps = new int[console.nextInt()];
            double average = 0;
            int overAverage = 0;
            
            for(int i = 0; i < temps.length; i++){
                  System.out.printf("Day %d's high temp: ", i+1);
                  temps[i] = console.nextInt();
                  average += temps[i];
            }
            
            average /= temps.length;
            
            for(int i : temps){
                  if(i > average)
                        overAverage++;
            }
            
            System.out.printf("Average temp = %.1f\n", average);
            System.out.printf("%d days above average", overAverage);
      }
}