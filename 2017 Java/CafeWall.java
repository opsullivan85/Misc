//Owen Sullivan 10/23
//Java Period: 7
//CafeWall Project
//This code draws an illusion 

//Import statement to allow use of the graphics panel
import java.awt.*;

//Main class 
public class CafeWall {
      
      //Main method which calls the other methods and sets up drawing panel
      public static void main(String[] args){
            
            //Sets up the drawing panel for use
            DrawingPanel panel = new DrawingPanel(650, 400); 
            panel.setBackground(Color.GRAY);
            Graphics g = panel.getGraphics();
            
            //Calling methods to draw shapes
            drawRow(g, 0, 0, 20, 4);
            drawRow(g, 50, 70, 30, 5);
            drawGrid(g, 10, 150, 26, 4, 8, 0);
            drawGrid(g, 250, 200, 25, 3, 6, 10);
            drawGrid(g, 425, 180, 20, 5, 10, 10);
            drawGrid(g, 400, 20, 35, 2, 4, 35);
            //Format drawGrid(graphics, xpos, ypos, size, len, rows, offset);
      }
      
      //Method that draws black square and a white square
      public static void drawPair(Graphics g, int x, int y, int size){
            
            g.setColor(Color.BLACK);
            g.fillRect(x, y, size, size);
            
            g.setColor(Color.BLUE);
            g.drawLine(x, y, x + size - 1, y + size - 1);
            g.drawLine(x + size - 1, y, x, y + size - 1);
            
            g.setColor(Color.WHITE);
            g.fillRect(x + size, y, size, size);
            
      }
      
      //Method that draws a row of black and white squares
      public static void drawRow(Graphics g, int x,  int y, int size, int len){
            
            for(int i = 0; i < len; i++){
                  drawPair(g, x + size * 2 * i , y, size);
            }
      }
      
      //Method that draws a grid composed of rows, and also makes the offset
      public static void drawGrid(Graphics g, int x,  int y, int size, int len, int rows, int offset){
            
            for(int r = 0; r < rows; r++){
                  drawRow(g, x + (r % 2 * offset), y + r * (size + 2), size, len);
                  
            }
      }
}
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            