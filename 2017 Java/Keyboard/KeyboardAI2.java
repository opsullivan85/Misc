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
            //pop.print(false, false, false, true, false);
            //pop.print(true, true, false, true, true);
            //pop.showGenOverview();
            while(pop.gen < 2){
                  //System.out.println("--------------------------------------------------");
                  pop.naturalSelection();
                  //pop.showGenOverview();
                  System.out.println(pop.gen);
            }
            pop.showGenOverview();
            System.out.println("--------------------------------------------------");
            pop.print(true, true, false, true, true);
            
            //System.out.println("Fitness: " + qwerty.fitness);
            //pop.getBestPlayer();
            //System.out.println("Worst Fitness = " + pop.bestFitness);
            //qwertyKeyboard();
            
      }
      
      public static void qwertyKeyboard(){
            Keyboard qwerty = new Keyboard(new Random());
            qwerty.board1D = new char[]{'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'};
            qwerty.updateBoard();
            qwerty.printBoard();
            qwerty.printBoard();
            //qwerty.getFitness();
            //System.out.println("Fitness: " + qwerty.fitness);
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

      public Keyboard(){
            Random rand = new Random();
            for(char i = 97; i <= 122; i++){
                  this.board1D[i-97] = i;
            }
            randomize(rand);
            updateBoard();
            homeRow();
      }
      
      public Keyboard(Random rand){
            for(char i = 97; i <= 122; i++){
                  this.board1D[i-97] = i;
            }
            randomize(rand);
            updateBoard();
            homeRow();
      }
      
      public Keyboard(Keyboard kb2Copy){
            this.board1D = kb2Copy.board1D.clone();
            this.board = kb2Copy.board.clone();
            this.keyCoords = kb2Copy.keyCoords.clone();
            this.fingers = kb2Copy.fingers.clone();
            this.fitness = kb2Copy.fitness;
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
      
      public void updateBoard1D(){
            int i = 0;
            for(int row = 0; row < this.board.length; row++){
                  for(int col = 0; col < this.board[row].length; col++){
                        this.board1D[i] = this.board[row][col];
                        i++;
                  }
            }
      }
      
      public void randomize(Random rand){
            for(int i = 0; i < this.board1D.length; i++)
                  this.swap(i, rand.nextInt(this.board1D.length-1));
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
           this.fitness = this.fitness/100-75;
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
      
      public void mutate(){
            Random rand = new Random();
            double rand1 = rand.nextDouble();
            double rand2 = rand.nextDouble();
            if(rand1 < 1){ //mutate 80% of the time
                  if(rand2 < 0.05){ //5% randomize whole board
                        this.randomize(rand);
                        this.updateBoard();
                  } else if(rand2 < 0.2){ //10% randomize row
                        int row = rand.nextInt(3);
                        for(int col = 0; col < this.board[row].length; col++){
                              int destCol = rand.nextInt(this.board[row].length);
                              char tmp = this.board[row][col];
                              this.board[row][col] = this.board[row][destCol];
                              this.board[row][destCol] = tmp;
                        }
                        this.updateBoard1D();
                  } else if(rand2 < 0.3){ //10% randomize col
                        int col = rand.nextInt(9);
                        int maxRow = (col < 7) ? 3 : 2;
                        for(int row = 0; row < maxRow; row++){
                              int destRow = rand.nextInt(maxRow);
                              char tmp = this.board[row][col];
                              this.board[row][col] = this.board[destRow][col];
                              this.board[destRow][col] = tmp;
                        }
                        this.updateBoard1D();
                  } else if(rand2 < 0.3){ //10% swap 3&4 && 5&6
                        char tmp3;
                        char tmp6;
                        for(int row = 0; row < this.board.length; row++){
                              tmp3 = this.board[row][3];
                              this.board[row][3] = this.board[row][4];
                              this.board[row][4] = tmp3;
                              tmp6 = this.board[row][6];
                              this.board[row][6] = this.board[row][5];
                              this.board[row][5] = tmp6;
                        }
                        this.updateBoard1D();
                  } else{ //Remaining change swap 2 random keys
                        this.swap(rand.nextInt(this.board1D.length), rand.nextInt(this.board1D.length));
                        this.updateBoard();
                  }
            }
      }
}

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

class Population {
      
      Keyboard[] boards;
      int gen = 0;
      int bestPlayerIndex = 0;
      double fitnessSum = 0;
      double bestFitness = 0;
      long t0 = System.currentTimeMillis();
      
      public Population(int size){
            boards = new Keyboard[size];
            for(int i = 0; i < size; i++){
                  boards[i] = new Keyboard(new Random());
            }
      }
      
      public void naturalSelection(){
            Keyboard[] newBoards = new Keyboard[this.boards.length];
            this.getFitnesses();
            this.getFitnessSum();
            this.getBestPlayer();
            newBoards[0] = new Keyboard(this.boards[this.bestPlayerIndex]);
            for(int i = 1; i < this.boards.length; i++){
                  newBoards[i] = new Keyboard(this.selectBoard());
                  newBoards[i].mutate();
            }
            this.boards = newBoards.clone();
            gen++;
      }
      
      public void getFitnesses(){
            for(int i = 0; i < this.boards.length; i++){
                  this.boards[i].getFitness();
            }
      }
      
      public void getFitnessSum(){
            this.fitnessSum = 0;
            for(int i = 0; i < this.boards.length; i++){
                  this.fitnessSum += this.boards[i].fitness;
            }
      }
      
      public Keyboard selectBoard(){
            double runningSum = 0;
            double randVal = new Random().nextDouble()*this.fitnessSum;
            for(int i = 0; i < this.boards.length; i++){
                  runningSum += this.boards[i].fitness;
                  if(runningSum > randVal){
                        return new Keyboard(this.boards[i]);
                  }
            }
            return this.boards[0];
      }
      
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
      
      public void showGenOverview(){
            System.out.println("Generation: " + this.gen);
            System.out.println("  *Best Board: #" + this.bestPlayerIndex);
            this.boards[bestPlayerIndex].printBoard(4);
            System.out.println("  *Fitness: " + this.bestFitness);
            System.out.println("  *Average Fitness: " + (this.fitnessSum/this.boards.length));
            fTime(System.currentTimeMillis()-t0);
      }
      
      public void fTime(long t){
            
            int h = (((int)(t)/1000)/60)/60;
            int m = (((int)(t)/1000)/60)%60;
            int s = ((int)(t)/1000)%60;
            int ms = (int)(t)%1000;
            
            System.out.printf("  *Time Elapsed: %d h %d m %d s & %d ms\n", h, m, s, ms);
      }
}



































