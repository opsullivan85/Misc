import java.util.*;

public class TooMuchHomework{
      public static void main(String[] args){
            
            Scanner console = new Scanner(System.in);
            
            System.out.print("Does she do homework? ");
            
            if (console.next().toLowerCase().charAt(0) == 'y'){
                  System.out.println("Yes"); 
            } else {
                  System.out.println("No");
            }
      }
}