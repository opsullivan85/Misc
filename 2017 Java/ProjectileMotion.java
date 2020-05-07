import java.util.*;

class ProjectileMotion {
      public static void main(String[] args){
            Scanner console = new Scanner(System.in);
            projectileMotion(console);
      }
      
      public static void projectileMotion(Scanner console){
            
            System.out.print("Initial Height(m): ");
            double y0 = console.nextDouble();
            System.out.print("Initial Angle: ");
            double angle = console.nextDouble();
            System.out.print("Initial Velocity(m/s): ");
            double v0 = console.nextDouble();
            
            double v0x = v0*Math.cos(angle);
            double v0y = v0*Math.sin(angle);
            double g = -9.81;
            
            double time = (-v0y+Math.sqrt((v0y*v0y)-(19.62*y0)))/(2*y0);
            double range = (v0x*time);
            double maxHeight = (((v0*v0)*Math.sin(Math.sin(angle)))/(2*g)+y0);
            
            
            System.out.println("Time(s) = " + time);
            System.out.println("Range(m) = " + range);
            System.out.println("Max Height()m = " + maxHeight);
      }            
}