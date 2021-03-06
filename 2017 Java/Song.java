//Owen Sullivan 9/10
//Java Period: 7
//Song Project
//This Project Prints an Abridged Version of "Bought Me A Cat"

public class Song {

      //The main method that prints all of the stanzas together
      public static void main(String[] args) {
            verseOne();
            verseTwo();
            verseThree();
            verseFour();
            verseFive();
            verseSix();
      }
  
      //Prints stanza one
      public static void verseOne() {
            System.out.println("Bought me a cat and the cat pleased me,");
            System.out.println("I fed my cat under yonder tree.");
            cat();
      }
 
      //Prints stanza two
      public static void verseTwo() {
            System.out.println("Bought me a hen and the hen pleased me,");
            System.out.println("I fed my hen under yonder tree.");
            hen();
      }
  
      //Prints stanza three
      public static void verseThree() {
            System.out.println("Bought me a duck and the duck pleased me,");
            System.out.println("I fed my duck under yonder tree.");
            duck();
      }
  
      //Prints stanza four
      public static void verseFour() {
            System.out.println("Bought me a goose and the goose pleased me,");
            System.out.println("I fed my goose under yonder tree.");
            goose();
      }
  
      //Prints stanza five
      public static void verseFive() {
            System.out.println("Bought me a sheep and the sheep pleased me,");
            System.out.println("I fed my sheep under yonder tree.");
            sheep();
      }
      
      //Prints stanza six
      public static void verseSix() {
            System.out.println("Bought me a pig and the pig pleased me,");
            System.out.println("I fed my pig under yonder tree.");
            pig();
      }
      
      //Prints the pig, and its noises, then calls the next animal down the line
      public static void pig() {
            System.out.println("Pig goes oink, oink,");
            sheep();
      }
      
      //Prints the sheep, and its noises, then calls the next animal down the line
      public static void sheep() {
            System.out.println("Sheep goes baa, baa,");
            goose(); 
      }
      
      //Prints the goose, and its noises, then calls the next animal down the line
      public static void goose() {
            System.out.println("Goose goes hissy, hissy,");
            duck();
      }
      
      //Prints the duck, and its noises, then calls the next animal down the line
      public static void duck() {
            System.out.println("Duck goes quack, quack,");
            hen();
      }
      
      //Prints the hen, and its noises, then calls the next animal down the line
      public static void hen() {
            System.out.println("Hen goes chimmy-chuck, chimmy-chuck,");
            cat();
      }
      
      //Prints the cat, and its noises, then calls the next animal down the line
      public static void cat() {
            System.out.println("Cat goes fiddle-i-fee.");
            System.out.println("");
      }
      
}
