public class Numbers {
      public static void main(String[] args) {
            int number = 42;
            int sum = 0;
            for (int i = 1; i <= 1000; i++){
                  number = number * 37 % 103;
                  sum++;
            }
            int number2 = number * number;
            System.out.println("result = " + number2);
      }
}