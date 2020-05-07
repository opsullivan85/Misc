import java.io.*;

public class Test {
      
      public static void main(String[] args) { 
            try {
                  File file = new File("test.csv");
                  file.createNewFile();
                  
                  PrintWriter printWriter = new PrintWriter(file);
                  printWriter.println("This is ");
                  printWriter.print("a test");
                  printWriter.flush();
                  printWriter.close();
            } catch (IOException e) {
                  e.printStackTrace();
            }
      }
}
//"C/Users/opsul/Desktop/file.txt"