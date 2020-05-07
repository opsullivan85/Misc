import java.util.*;

public class GansterName {
      public static void main(String[] args){
            Scanner console = new Scanner(System.in);
            
            System.out.println("Please enter your name");
            
            String nameFirst = console.next();
            String nameLast = console.next();
            
            System.out.println(nameFirst.substring(0,1) + ". Diddy " + nameLast.toUpperCase() +" " + nameFirst + "-issle");
      }
}
            