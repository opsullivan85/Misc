class PerfectNumbers{
      
      public static void main(String[] args){
            perfectNumbers(1000000000);
      }
      
      public static void perfectNumbers(int n) { 
            System.out.print("Perfect numbers up to " + n + ": ");
            
            for(int i = 1; i <= n; i++){
                  double sum = 0.0;
                  
                  for(double a = 1.0; a < i; a++){
                        if(i % a == 0.0){
                              sum += a;
                        }
                  }
                  
                  if(sum == i)
                        System.out.print(i + " ");
            }
      }
}