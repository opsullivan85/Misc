//Owen Sullivan 12/15
//Java Period: 7
//RandomWalk Project
//This code performs a random walk given the users parameters

import java.awt.*;
import java.util.*;

public class RandomWalk{
      
      public static final boolean DEBUG = false;
      public static final int SIZE = 1000;
      
      public static void main(String[] args){
            
            DrawingPanel panel = new DrawingPanel(SIZE, SIZE);
            Graphics g = panel.getGraphics();
            Scanner console = new Scanner(System.in);
            Random rand = new Random();
            
            //Prints introduction
            System.out.println("This program performs a random walk given your parameters");
            System.out.println();
            
            promptUser(rand, console, g, panel);
      }
      
      //Method prompts the user for the parameters for their random walk.
      public static void promptUser(Random rand, Scanner console, Graphics g, DrawingPanel panel){
            boolean reRun = true;
            int totalSteps = 0;
            int totalWalks = 0;
            int bestWalk = 0;
            int runsMoves = 0;
            int stepSize;
            int radius;
            String response;
            
            //Runs the random walk, while the user would like to re-run.
            while(reRun){
                  panel.clear();
                  System.out.print("Step size? ");
                  stepSize = console.nextInt();
                  
                  System.out.print("Radius? ");
                  radius = console.nextInt();
                  
                  runsMoves = walk(rand, g, stepSize, radius);
                  totalSteps += runsMoves;
                  
                  if (totalWalks == 0 || runsMoves < bestWalk)
                        bestWalk = runsMoves;
                  
                  totalWalks++;
                  
                  System.out.print("Walk again (yes/no)? ");
                  response = console.next();
                  
                  reRun = (response.toLowerCase().charAt(0) == 'y');
                  
                  System.out.println();
            }
            
            //Prints out statistics.
            System.out.println("Total walks = " + totalWalks);
            System.out.println("Total steps = " + totalSteps);
            System.out.println("Best walk   = " + bestWalk);
      }
      
      //Method which given parameters from promptUser() performs an entire random walk.
      public static int walk(Random rand, Graphics g, int stepSize, int radius){
            Point center = new Point(radius, radius);
            Point pos = new Point(center);
            int moves = 0;
            int x, y;
            
            //Draws the circle.
            g.drawOval(0, 0, 2 * radius, 2 * radius);
            
            //Moves point and draws squares while inside the confining circle
            while(center.distance(pos)<=radius){
                  pos.setLocation(randStep(rand, g, stepSize, pos));
                  moves++;
                  
                  //Prints the 'Debug' information.
                  if(DEBUG){
                        x = (int)pos.getX();
                        y = (int)pos.getY();
                        System.out.printf("x=%d, y=%d, moves=%d\n", x, y, moves);
                  }
            }
            
            System.out.printf("I escaped in %d move(s).\n", moves);
            
            return moves;
      }
      
      //Method which given the current position and a stepsize, returns a point with
      //a distance 'stepsize' from the current position in an orthagonal direction.
      public static Point randStep(Random rand, Graphics g, int stepSize, Point pos){
            int stepDirection = rand.nextInt(4);
            
            //Changes to a random color.
            Color randColor = new Color(rand.nextInt(256),rand.nextInt(256),rand.nextInt(256));
            g.setColor(randColor);
            
            if(stepDirection == 0){
                  g.fillRect((int)pos.getX(), (int)pos.getY(), stepSize, stepSize);
                  pos.translate(stepSize, stepSize);
            }
            else if(stepDirection == 1){
                  g.fillRect((int)pos.getX()-stepSize, (int)pos.getY(), stepSize, stepSize);
                  pos.translate(-stepSize, stepSize);
            }
            else if(stepDirection == 2){
                  g.fillRect((int)pos.getX()-stepSize, (int)pos.getY()-stepSize, stepSize, stepSize);
                  pos.translate(-stepSize, -stepSize);
            }
            else{
                  g.fillRect((int)pos.getX(), (int)pos.getY()-stepSize, stepSize, stepSize);
                  pos.translate(stepSize, -stepSize);
            }
            
            return pos;
      }
}