import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.lang.*;
import java.math.*;

/*----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q W E R T Y U I O P
A S D F G H J K L _
Z X C V B N M _ _ _

0 1 2 3 3 6 6 7 8 9
0 1 2 3 3 6 6 7 8 _
0 1 2 3 3 6 6 _ _ _

Q W E R T Y U I O P|A S D F G H J K L _|Z X C V B N M _ _ _ -- 30
0 1 2 3 3 6 6 7 8 9|0 1 2 3 3 6 6 7 8 _|0 1 2 3 3 6 6 _ _ _ -- 30
0 1 2 3 4 5 6 7 8 9|0 1 2 3 4 5 6 7 8 _|9 1 2 3 4 5 6 _ _ _ 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

class KeyboardAI2{
      Random rand = new Random();
      public static void main(String[] args){
            Population pop = new Population(10);
            //pop.getFitnesses();
            pop.print(false, false, false, true, false);
            //pop.print(false, true, false, true, true);
            System.out.println("Fitness: " + qwerty.fitness);
            qwertyKeyboard();
      }
      
      public static void qwertyKeyboard(){
            Keyboard qwerty = new Keyboard(new Random());
            qwerty.board1D = new char[]{'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'};
            qwerty.updateBoard();
            //qwerty.printBoard();
            qwerty.getFitness();
            System.out.println("Fitness: " + qwerty.fitness);
      }
}

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

class Keyboard {
      public char[] board1D = new char[26];
      public char[][] board = {new char[10], new char[9], new char[7]};
      public int[][] keyCoords = new int[26][2];
      public boolean[][] fingers = new boolean[3][10];
      public double fitness = 0;
      static boolean[] HOME_ROW;
      static String WORD_LIST;
      static int WORD_LIST_LENGTH;
      
      static{
            HOME_ROW = new boolean[]{true, true, true, true, false, false, true, true, true, true};
            try{
                  WORD_LIST = new String(Files.readAllBytes(Paths.get("WordList10000ByFreq.txt")));
                  WORD_LIST_LENGTH = WORD_LIST.length();
            } catch(IOException e){
                  System.out.println("ERROR! Cannot find file!");
            }
      };

      public Keyboard(Random rand){
            for(char i = 97; i <= 122; i++){
                  this.board1D[i-97] = i;
            }
            randomize(rand);
            updateBoard();
            homeRow();
      }
      
      public void updateBoard(){
            int i = 0;
            for(int row = 0; row < this.board.length; row++){
                  for(int col = 0; col < this.board[row].length; col++){
                        this.board[row][col] = this.board1D[i];
                        keyCoords[this.board1D[i]-97][0] = row;
                        keyCoords[this.board1D[i]-97][1] = col;
                        i++;
                  }
            }
      }
      
      public void randomize(Random rand){
            for(int i = 0; i < this.board1D.length; i++)
                  swap(i, rand.nextInt(this.board1D.length-1));
      }
      
      public void swap(int ind1, int ind2){
            char temp = this.board1D[ind1];
            this.board1D[ind1] = this.board1D[ind2];
            this.board1D[ind2] = temp;
      }
      
      public void printBoard(){
            for(int row = 0; row < this.board.length; row++){
                  for(int col = 0; col < this.board[row].length; col++){
                        System.out.printf("%c ", this.board[row][col]);
                  }
                  System.out.println();
            }
      }
      
      public void printFingers(){
            for(int row = 0; row < this.fingers.length; row++){
                  for(int col = 0; col < this.fingers[row].length; col++){
                        if(this.fingers[row][col]){
                              System.out.print("O");
                        } else{
                              System.out.print(".");
                        }
                  }
                  System.out.println();
            }
      }
      
      public void printBoard(int spaces){
            for(int row = 0; row < this.board.length; row++){
                  for(int i = spaces; i > 0; i--)
                        System.out.print(" ");
                  for(int col = 0; col < this.board[row].length; col++){
                        System.out.printf("%c ", this.board[row][col]);
                  }
                  System.out.println();
            }
      }
      
      public void printFingers(int spaces){
            for(int row = 0; row < this.fingers.length; row++){
                  for(int i = spaces; i > 0; i--)
                        System.out.print(" ");
                  for(int col = 0; col < this.fingers[row].length; col++){
                        if(this.fingers[row][col]){
                              System.out.print("O");
                        } else{
                              System.out.print(".");
                        }
                  }
                  System.out.println();
            }
      }
      
      public void getFitness(){
            int wordFitness = 0;
            int wordCount = 0;
            int letterCount = 0;
            int[] coords;
            char letter;
            for(int i = 0; i < WORD_LIST_LENGTH; i++){
                  if(WORD_LIST.charAt(i)==10){
                        wordCount++;
                        this.fitness += Math.pow(wordFitness, 2)*(7./wordCount);
                        wordFitness = 0;
                        letterCount = 0;
                        homeRow();
                  } else {
                        //coords = keyCoords[WORD_LIST.charAt(i)-97];
                        letterCount++;
                        wordFitness += dstFromFinger(this.keyCoords[WORD_LIST.charAt(i)-97]);
                  }
            }
           //this.fitness = this.fitness;
      }
      
      public int dstFromFinger(int[] coords){// !LOWER = MORE FIT
            if(this.fingers[coords[0]][coords[1]]){ //Finger already on key
                  return 3-0;
            } else if(coords[1] <= 2 || coords[1] >= 7){
                  for(int row = 0; row < 3; row++){
                        if(this.fingers[row][coords[1]]){
                              this.fingers[row][coords[1]] = false;
                              this.fingers[coords[0]][coords[1]] = true;
                              return 3-Math.abs(row-coords[0]);
                        }
                  }
            } else if(coords[1] == 3 || coords[1] == 5){
                  for(int row = 0; row < 3; row++){
                        if(this.fingers[row][coords[1]]){ // Finger in same col
                              this.fingers[row][coords[1]] = false;
                              this.fingers[coords[0]][coords[1]] = true;
                              return 3-Math.abs(row-coords[0]);
                        } else if(this.fingers[row][coords[1]+1]){
                              this.fingers[row][coords[1]+1] = false;
                              this.fingers[coords[0]][coords[1]+1] = true;
                              return 3-Math.abs(row-coords[0])+1;
                        }
                  }
            } else if(coords[1] == 4 || coords[1] == 6){
                  for(int row = 0; row < 3; row++){
                        if(this.fingers[row][coords[1]]){
                              this.fingers[row][coords[1]] = false;
                              this.fingers[coords[0]][coords[1]] = true;
                              return 3-Math.abs(row-coords[0]);
                        } else if(this.fingers[row][coords[1]-1]){
                              this.fingers[row][coords[1]-1] = false;
                              this.fingers[coords[0]][coords[1]-1] = true;
                              return 3-Math.abs(row-coords[0])+1;
                        }
                  }
            }
            return 3-0;
      }
      
      public void homeRow(){
            for(int row = 0; row < this.fingers.length; row++)
                  Arrays.fill(this.fingers[row], false);
            for(int col = 0; col < fingers[1].length; col++)
                  this.fingers[1][col] = HOME_ROW[col];
      }
}

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

class Population {
      
      Keyboard[] boards;
      int gen = 1;
      int bestPlayerIndex = 0;
      double fitnessSum = 0;
      double bestFitness = 0;
      
      public Population(int size){
            boards = new Keyboard[size];
            for(int i = 0; i < size; i++){
                  boards[i] = new Keyboard(new Random());
            }
      }
      
      public void getFitnesses(){
            for(int i = 0; i < this.boards.length; i++){
                  this.boards[i].getFitness();
            }
      }
      
      public void getFitnessSum(){
            for(int i = 0; i < this.boards.length; i++){
                  this.fitnessSum += this.boards[i].fitness;
            }
      }
      
      //public Keyboard selectBoard(){
      
      public void getBestPlayer(){
            this.bestPlayerIndex = 0;
            this.bestFitness = this.boards[0].fitness;
            for(int i = 1; i < this.boards.length; i++){
                  if(this.bestFitness < this.boards[i].fitness){ //If selected player has better fitness
                        this.bestFitness = this.boards[i].fitness;
                        this.bestPlayerIndex = i;
                  }
            }
      }
      
      public void print(){
            for(int i = 0; i < this.boards.length; i++){
                  System.out.println("Board #" + (i+1) + ":");
                  System.out.println("  *Board:");
                  this.boards[i].printBoard(4);
                  System.out.println("  *Fingers:");
                  this.boards[i].printFingers(4);
                  System.out.println("  *Fitness: " + this.boards[i].fitness);
                  System.out.println();
            }
      }
      
      public void print(boolean boardNum, boolean boards, boolean fingers, boolean fitnesses, boolean seperation){
            for(int i = 0; i < this.boards.length; i++){
                  if(boardNum){
                        System.out.println("Board #" + (i+1) + ":");
                        if(boards){
                              System.out.println("  *Board:");
                              this.boards[i].printBoard(4);
                        }
                        if(fingers){
                              System.out.println("  *Fingers:");
                              this.boards[i].printFingers(4);
                        }
                        if(fitnesses){
                              System.out.println("  *Fitness: " + this.boards[i].fitness);
                        }
                  } else{
                        if(boards){
                              this.boards[i].printBoard(0);
                        }
                        if(fingers){
                              this.boards[i].printFingers(0);
                        }
                        if(fitnesses){
                              System.out.println("Fitness: " + this.boards[i].fitness);
                        }
                  }
                  if(seperation){
                        System.out.println();
                  }
            }
      }
}



































