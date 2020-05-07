//Owen Sullivan 10/1
//Java Period: 7
//SpaceNeedle Project
//This code prints a tower that is scalable by use of a constant

public class SpaceNeedle{
      
      //The constant which can be changed to determine the size of the tower
      public static final int TOWER_SIZE = 6;
      
      //The main method which runs all other methods in the required order to print the tower
      public static void main(String[] args){
            printNeck();
            printFoot();
            printBottom();
            printNeck();
            printColumn();
            printFoot();
      }
      
      //Prints out the "Neck" of the tower
      public static void printNeck(){
            for (int row = 1; row <= TOWER_SIZE; row++){
                  for (int i = 1; i <= (3 * TOWER_SIZE); i++){
                        System.out.print(" ");
                  }
                  
                  System.out.println("||");
            }
      }
      
      //Prints out the "Foot" of the tower
      public static void printFoot(){
            for (int row = 1; row <= TOWER_SIZE; row++){
                  for (int i = 1; i <= ((3 * TOWER_SIZE) - (3 * row)); i++){
                        System.out.print(" ");
                  }
                  
                  System.out.print("__/");
                  
                  for (int i = 1; i <= (row - 1); i++){
                        System.out.print(":::");
                  }
                  
                  System.out.print("||");
                  
                  for (int i = 1; i <= (row - 1); i++){
                        System.out.print(":::");
                  }
                  
                  System.out.println("\\__");
            }
            
            System.out.print("|");
            
            for (int i = 1; i <= TOWER_SIZE; i++){
                  System.out.print("\"\"\"\"\"\"");
            }
            
            System.out.println("|");
      }
      
      //Prints out the "Bottom" of the tower
      public static void printBottom(){
            for (int row = 1; row <= TOWER_SIZE; row++){
                  for (int i = 1; i <= (2 * row - 2); i++){
                        System.out.print(" ");
                  }
                  
                  System.out.print("\\_");
                  
                  for (int i = 1; i <= ((3 * TOWER_SIZE - 1) - (2 * row - 2)); i++){
                        System.out.print("/\\");
                  }
                  
                  System.out.println("_/");
            }
      }
      
      //Prints out the "Column" of the tower
      public static void printColumn(){
            for (int row = 1; row <= (TOWER_SIZE * TOWER_SIZE); row++){
                  for (int i = 1; i <= (2 * TOWER_SIZE + 1); i++){
                        System.out.print(" ");
                  }
                  
                  System.out.print("|");
                  
                  for (int i = 1; i <= (TOWER_SIZE - 2); i++){
                        System.out.print("%");
                  }
                  
                  System.out.print("||");
                  
                  for (int i = 1; i <= (TOWER_SIZE - 2); i++){
                        System.out.print("%");
                  }
                  
                  System.out.println("|");
            }
      }
}