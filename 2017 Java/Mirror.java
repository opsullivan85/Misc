public class Mirror {
      
      public static final int SIZE = 15;
      
      public static void main(String[] args) {
            line();
            topHalf();
            bottomHalf();
            line();
      }
      
      public static void topHalf() {
            for (int line = 1; line <= SIZE; line++) {
                  System.out.print("|");
                  
                  for (int space = 1; space <= (-2 * line + 2*SIZE); space++){
                        System.out.print(" ");
                  }
                  
                  System.out.print("<>");
                  
                  for (int dot = 1; dot <= (4 * line - 4); dot++){
                        System.out.print(".");
                  }
                  
                  System.out.print("<>");
                  
                  for (int space = 1; space <= (-2 * line + 2*SIZE); space++){
                        System.out.print(" ");
                  }
                  
                  System.out.println("|");
                  
                  // contents of each line
            }
      }
      
      public static void bottomHalf() {
            for (int line = 1; line <= SIZE; line++) {
                  System.out.print("|");
                  
                  for (int space = 1; space <= (2 * line - 2); space++){
                        System.out.print(" ");
                  }
                  
                  System.out.print("<>");
                  
                  for (int dot = 1; dot <= (-4 * line + 4*SIZE); dot++){
                        System.out.print(".");
                  }
                  
                  System.out.print("<>");
                  
                  for (int space = 1; space <= (2 * line - 2); space++){
                        System.out.print(" ");
                  }
                  
                  System.out.println("|");
                  // contents of each line
            }
      }

      public static void line() {
            
            System.out.print("#");
            for (int line = 1; line <= 4*SIZE; line++){
                  System.out.print("-");
            }
            
            System.out.println("#");
            
      }
}