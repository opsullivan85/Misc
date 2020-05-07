class Vowel{
      public static void main(String[] args){
            System.out.println(isVowel("O"));
      }
      
      public static boolean isVowel(String string){
            string = string.toLowerCase();
            return (string.equals("a") || string.equals("e") || string.equals("i") || string.equals("o") || string.equals("u"));
      }
      
      public static boolean isNonVowel(String string){
            return !isVowel(string);
      }
}