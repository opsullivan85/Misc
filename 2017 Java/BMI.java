import java.util.*;

public class BMI {
      public static void main(String[] args){
            
            System.out.println("This program reads data for two people and");
            System.out.println("computes their body mass index (BMI).");
            System.out.println();
            
            Scanner console = new Scanner(System.in);
            
            double person1BMI = getBMI(console);
            double person2BMI = getBMI(console);
            
            info(person1BMI, 1);
            info(person2BMI, 2);
            
            System.out.println("Difference = " + (person1BMI - person2BMI));
      }
      
      public static double getBMI(Scanner console){
            System.out.println("Enter next person's information:");
            
            System.out.print("height (in inches)? ");
            double height = console.nextDouble();
            
            System.out.print("weight (in pounds)? ");
            double weight = console.nextDouble();
            
            System.out.println();
            
            return (weight/(height*height))*703;
      }
      
      public static void info(double personBMI, int personNum){
            System.out.println("Person " + personNum + " BMI = " + personBMI);
            if (personBMI < 18.5)
                  System.out.println("underweight");
            else if (personBMI < 25)
                  System.out.println("normal");
            else if (personBMI < 30)
                  System.out.println("normal");
            else
                  System.out.println("obese");
      }
}
                  
            
            