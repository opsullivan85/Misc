class Zeros{
      public static void main(String[] args){
            System.out.println(zeroDigits(5024036));
      }
      public static int zeroDigits(int number){
            int count = 1;
            int mod = 0;
            int zeros = 0;
            do {
                  mod = (number/count)%10;
                  if(mod == 0)
                        zeros++;
                  count *= 10;
            } while(count < number);
                  return zeros;
      }
}