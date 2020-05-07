public class ASCII{
      public static void main(String[] args){
            for (char i = 33; i <= 255; i++){
                  System.out.printf("%c ", i);
                  if (i % 16 == 0){
                        System.out.println();
                  }
            }
      }
}