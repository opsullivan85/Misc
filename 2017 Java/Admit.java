//Owen Sullivan 12/5
//Java Period: 7
//Admit Project
//This code determines which of two applicants is better

//Import statement to allow use of the Scanner class
import java.util.*;


class Admit{
      //Main method which calls the other methods
      public static void main(String[] args){
            Scanner console = new Scanner(System.in);
            
            //Prints the introduction
            introduction();
            
            //Gets the information for each of the two applicants
            double applicantOne = applicantInfo(console, 1);
            double applicantTwo = applicantInfo(console, 2);
            
            //Compares the applicants, and prints which is better
            compare(applicantOne, applicantTwo);
      }
      
      //Prints out the introduction text
      public static void introduction(){
            System.out.println("This program compares two applicants to");
            System.out.println("determine which one seems like the stronger");
            System.out.println("applicant.  For each candidate I will need");
            System.out.println("either SAT or ACT scores plus a weighted GPA.\n");
      }
      
      //When passed two applicant scores, determines which applicant is better
      public static void compare(double applicantOne, double applicantTwo){
            System.out.printf("First applicant overall score  = %.1f\n", applicantOne);
            System.out.printf("Second applicant overall score = %.1f\n", applicantTwo);
            
            //Ditermines which applicant is better, then prints the answer
            if(applicantOne > applicantTwo)
                  System.out.println("The first applicant seems to be better");
            else
                  System.out.println("The first applicant seems to be better");
      }
      
      //Calls functions to get the applicant's information, and then returns their overall score
      public static double applicantInfo(Scanner console, int applicantNumber){
            System.out.printf("Information for applicant #%d:\n", applicantNumber);
            
            double examScore = getExamScore(console);
            double gPA = getGPA(console);
            double overallScore = examScore + gPA;
            
            return overallScore;
      }
      
      //Requests the applicant's GPA information and then returns their GPA score
      public static double getGPA(Scanner console){
            System.out.print("    overall GPA?");
            double overallGPA = console.nextDouble();
            
            System.out.print("    max GPA");
            double maxGPA = console.nextDouble();
            
            System.out.print("    Transcript Multiplier?");
            double transcriptMultiplier = console.nextDouble();
            
            double gpaScore = ((overallGPA / maxGPA) * 100 * transcriptMultiplier);
            System.out.printf("    GPA score = %.1f\n\n", gpaScore);
            return gpaScore;
      }
      
      //Calls either getSAT or gatACT and then returns the applicant's exam score
      public static double getExamScore(Scanner console){
            System.out.print("    do you have 1) SAT scores or 2) ACT scores?");
            
            int testType = console.nextInt();
            double examScore = 0.0;
            
            //Calls either getSAT or getACT
            if(testType == 1){
                  examScore = getSAT(console);
            } else{
                  examScore = getACT(console);
            }
            
            System.out.printf("    exam score = %.1f\n", examScore);
            return examScore;
      }
                  
      //Requests the applicant's SAT scores, and then returns their score out of 100
      public static double getSAT(Scanner console){
            System.out.print("    SAT math?");
            int math = console.nextInt();
            
            System.out.print("    SAT critical reading?");
            int reading = console.nextInt();
            
            System.out.print("    SAT writing?");
            int writing = console.nextInt();
            
            double score = (2 * math + reading + writing) / 32;
            return score;
      }
      
      //Requests the applicant's ACT scores, and then returns their score out of 100
      public static double getACT(Scanner console){
            System.out.print("    ACT English?");
            int english = console.nextInt();
            
            System.out.print("    ACT math?");
            int math = console.nextInt();
            
            System.out.print("    ACT reading?");
            int reading = console.nextInt();
            
            System.out.print("    ACT science?");
            int science = console.nextInt();
            
            double score = (english + 2 * math + reading + science) / 1.8;
            return score;
      }
}