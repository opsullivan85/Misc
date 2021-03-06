//Owen Sullivan 1/8
//Java Period: 7
//Bagels Project
//This program plays, with the user, a game of Bagels, a variant of the game Mastermind
//Note: Method dividers are included to make methods easier to pick out

import java.util.*;

public class Bagels{
      
      public static final int LENGTH = 4;
      
      public static void main(String[] args){
            
            //Initialization
            Scanner console = new Scanner(System.in);
            Random rand = new Random();
            boolean replay = true;
            
            System.out.printf("$%.2/n", 123.456);
            
            //Prints introduction
            printIntroduction();
            
            //Plays the game
            do{
                  playGame(console, rand);
                  
                  System.out.print("Do you want to play again?");
                  if(console.next().toLowerCase().charAt(0) != 'y'){
                        replay = false;
                  }
                        
            } while(replay);
      }
      
      //Method runs one game
      public static void playGame(Scanner console, Random rand){
            
            //Initialization
            int[] guess = new int[LENGTH];
            int[] answer = new int[LENGTH];
            boolean hasWon;
            int guesses = 0;
            
            //Creates a randomly generated correct answer
            for(int i = 0; i < LENGTH; i++){
                  answer[i] = rand.nextInt(9)+1;
            }
            
            //Loop prompts user until answer is correct
            do{
                  guesses++;
                  
                  System.out.print("Your guess?");
                  guess = numToArray(console.nextInt());
                  
                  hasWon = giveHints(guess, answer);
                  
            } while(!hasWon);
            
            System.out.printf("You got it right in %d guesses.\n\n", guesses);
      }
      
      //Method gives hints given the users guess and the correct answer
      public static boolean giveHints(int[] guess, int[] answer){
            
            //Initialization
            int[] copyOfAnswer = Arrays.copyOf(answer, LENGTH);
            int fermiCount = countFermis(guess, copyOfAnswer);
            int picaCount = countPicas(guess, copyOfAnswer);
            
            if(fermiCount == LENGTH){
                  return true;
            }
            
            //Prints out hints
            if(fermiCount == 0 && picaCount == 0){
                  System.out.print("bagels");
            }
            
            for(int i = 1; i <= fermiCount; i++){
                  System.out.print("fermi ");
            }
            
            for(int i = 1; i <= picaCount; i++){
                  System.out.print("pica ");
            }
            
            System.out.println();
            
            return false;
      }
      
      //Method returns users "fermis" given their guess and the correct answer
      public static int countFermis(int[] guess, int[] answer){
            
            //Initialization
            int fermiCount = 0;
            
            //Counts fermis
            for(int i = 0; i < LENGTH; i++){
                  if(answer[i] == guess[i]){
                        fermiCount++;
                        answer[i] = -1;
                        guess[i] = 0;
                  }
            }
            
            return fermiCount;
      }
      
      //Method returns users "picas" given their guess and the correct answer
      public static int countPicas(int[] guess, int[] answer){
            
            //Initialization
            int picaCount = 0;
            
            //Counts picas
            for(int a = 0; a < LENGTH; a++){
                  for(int g = 0; g < LENGTH; g++){
                        if(answer[a] == guess[g]){
                              picaCount++;
                              answer[a] = -1;
                              guess[g] = 0;
                        }
                  }
            }
            
            return picaCount;
      }
      
      //Method returns an array, given an integer, with each index containing one of the digits
      public static int[] numToArray(int number){
            int[] digitArray = new int[LENGTH];
            
            for(int i = LENGTH-1; i >= 0; i--){
                  digitArray[i] = number % 10;
                  number /= 10;
            }
            
            return digitArray;
      }
      
      //Method prints the introduction
      public static void printIntroduction(){
            System.out.println("Welcome to Java Bagels!");
            System.out.printf("I'm thinking of a %d digit number.\n", LENGTH);
            System.out.println("Each digit is between 1 and 9.");
            System.out.println("Try to guess my number, and I'll say \"fermi\"");
            System.out.println("for each digit you get right, and \"pica\"");
            System.out.println("for each correct digit in the wrong place.");
            System.out.println();
      }
}