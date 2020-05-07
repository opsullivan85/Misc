class Anomaly{
      public static void main(String[] args){
            
            //Timer start
            long t0 = System.currentTimeMillis();
            
            //calls calls count a lot
            for (int h = 1; h <= 1000000000; h++){
                  for (int e = 1; e <= 1000000000; e++){
                        count();
                  }
            }
            //Has finished counting to one octilion
            //1,000,000,000,000,000,000,000,000,000
            //which is the same as counting to 
            //2^63 108,420,217 times!
            
            //BTW this math totally doesnt add up...
            //good GPUs can do 10^12 FPCs per 1000ms
            //this is logging 10^27 ICs in 25ms
            
            //Timer stop
            long t1 = System.currentTimeMillis();
            
            //Print Time
            System.out.println(t1-t0);
      }
      
      //Counts to 1000000000
      public static void count(){
            int d = 1000000000;
            int c = 0;
            while(c<=1000000000){
                                    //If you replace "1000000000" with "d" 
                                    //it takes 75 times as long to execute
                  c++;          
            }
      }
}