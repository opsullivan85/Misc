import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.lang.*;

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

class KeyboardAI{
      Random rand = new Random();
      public static void main(String[] args){
            Population pop = new Population(1);
            pop.print();
      }
}

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

class Keyboard {
      private char[] board1D = new char[26];
      public char[][] board = {new char[10], new char[9], new char[7]};
      public int[][] keyCoords = new int[26][2];
      public boolean[][] fingers = {new boolean[10], new boolean[9], new boolean[7]};
      
      static{
            try{
                  String WORDLIST = new String(Files.readAllBytes(Paths.get("WordList10000ByFreq.txt")));
            } catch(IOException e){
                  System.out.println("ERROR! Cannot find file!");
            }
      }

      public Keyboard(Random rand){
            for(char i = 97; i <= 122; i++){
                  this.board1D[i-97] = i;
            }
            randomize(rand);
            updateBoard();
            homeRow();
            for(int i = 0; i < 100; i++)
                  System.out.print(WORDLIST.charAt(i));
      }
      
      private void updateBoard(){
            int i = 0;
            for(int row = 0; row < this.board.length; row++){
                  for(int col = 0; col < this.board[row].length; col++){
                        this.board[row][col] = this.board1D[i];
                        keyCoords[this.board1D[i]-97][0] = row;
                        keyCoords[this.board1D[i]-97][1] = col;
                        i++;
                  }
            }
            System.out.print(this.keyCoords.toString());
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
      
      public void print(){
            for(int row = 0; row < this.board.length; row++){
                  for(int col = 0; col < this.board[row].length; col++){
                        System.out.printf("%c ", this.board[row][col]);
                  }
                  System.out.println();
            }
      }
      
      public double getFitness(){
            int wordCount = 0;
            return 0;
      }
      
      public double homeRow(){
            Arrays.fill(fingers, false);
            fingers[1] = HOME_ROW;
      }
}

/*--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

class Population {
      
      Keyboard[] boards;
      int gen = 1;
      int fitnessSum;
      
      public Population(int size){
            boards = new Keyboard[size];
            for(int i = 0; i < size; i++){
                  boards[i] = new Keyboard(new Random());
            }
      }
      
      public void print(){
            for(int i = 0; i < boards.length; i++){
                  boards[i].print();
            }
      }
}






































