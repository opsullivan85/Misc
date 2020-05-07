//Chapter 10 Project

//{ Includes
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <cctype>
#include <cstring>
#include <string>
//}

//{ Namespace
using namespace std;
//}

//{ Function Prototypes
char* uInputCStr();
void dispCStr(char*);
void backwardStr();
  void reverseStr(char*);
void sentenceCapitalizer();
  void capitalizer(char*);
void replaceSubstringFunction();
  string replaceSubstring(char*, char*, char*);
//}

int main(){
    cout << setprecision(1)<< left << fixed;
    backwardStr();
    sentenceCapitalizer();
    replaceSubstringFunction();
}

//{ Helpful Functions
//This function writes the user input to a string then copies that to a C-String
char* uInputCStr(){

    //Initialization
    string inputStr;
    char *inputCStr = nullptr;

    getline(cin, inputStr);

    //Allocates the C-String and copies the string to it
    int len = inputStr.length();
    inputCStr = new char[len+1];
    for(int i = 0; i < len; i++){
        inputCStr[i] = inputStr.at(i);
    }

    return inputCStr;
}

//This function accepts a C-String and then displays it
void dispCStr(char *cStr){
    int len = strlen(cStr);

    cout << "  ";
    for(int i = 0; i < len; i++)
        cout << cStr[i];

    cout << endl;
}
//}

//{ 2. Backward String
//This function prompts a user for a string and prints it backwards
void backwardStr(){
    cout << "2. Backward String" << endl;
    cout << "  Enter a string to be reversed:";

    //Passes the user input to reverseStr() which prints it out backwards
    reverseStr(uInputCStr());

    cout << endl;
}

//This function prints out the passed C-String backwards
void reverseStr(char *cStr){
    cout << "  ";
    for(int i = strlen(cStr) - 1; i >= 0; i--){
        cout << cStr[i];
    }
    cout << endl;
}
//}

//{ 5. Sentence Capitalizer
//This function prompts a user for a string and prints it with correct capitalization
void sentenceCapitalizer(){
    cout << "5. Sentence Capitalizer" << endl;
    cout << "  Enter a string to be capitalized: ";

    //Passes the user input to capitalizer() which capitalizes it where appropriate and prints the modified version
    capitalizer(uInputCStr());

    cout << endl;
}

//This function capitalizes the passed C-String and prints it
void capitalizer(char *cStr){
    //Goes through all characters of the C-String
    for(int i = 0; i < strlen(cStr) - 1; i++){
        //If the character at index i is punctuation this capitalizes the next non-space character
        if(ispunct(cStr[i])){
            //Increments i until it is the index of a non-space character
            do{
                i++;
            } while(isspace(cStr[i]));

            //Capitalizes the character at index i of the cStr
            cStr[i] = toupper(cStr[i]);
        }
    }

    //Capitalizes the first character of the cStr
    cStr[0] = toupper(cStr[0]);

    //Displays the cStr
    dispCStr(cStr);
}
//}

//{ 10. replaceSubstring Function
//This function prompts the user for three strings mainStr, subStr, and replacement
//All occurrences of the subStr in mainStr are replaced with replacement
void replaceSubstringFunction(){
    //Initialization
    char *mainStr, *subStr, *replacement;

    //Prompts user
    cout << "10. replaceSubstring Function" << endl;
    cout << "  Enter a string to modify: ";
    mainStr = uInputCStr();
    cout << "  Enter a substring to replace: ";
    subStr = uInputCStr();
    cout << "  Enter a replacement for substring: ";
    replacement = uInputCStr();

    //Prints out the modified string
    cout << "  " << replaceSubstring(mainStr, subStr, replacement);
    cout << endl;
}

//This function replaces all occurrences of the subStr in mainStr are replaced with replacement
string replaceSubstring(char *mainStr, char *subStr, char *replacement){
    //Initialization
    string newStr;
    int subStrLen = strlen(subStr);
    int replacementLen = strlen(replacement);
    int mainStrLen = strlen(mainStr);
    char *pos = nullptr;                                    //pos is a pointer to the address of the first occurrence of subStr in mainStr
    pos = strstr(mainStr, subStr);

    //Steps through all characters
    for(int i = 0; i < mainStrLen; i++){
        if(mainStr + i == pos){                             //If the address of mainStr[i] is equal to the pos pointer
            mainStr[i] = NULL;                              //Sets mainStr[i] to 'NULL' so that occurrence of subStr will be ignored in the future
            pos = strstr(mainStr, subStr);                  //Reassigns pos to the next occurence of subStr
            for(int n = 0; n < replacementLen; n++)         //Appends the replacement cStr to the end of newStr
                newStr += replacement[n];
            i += subStrLen;                                 //Steps i forwards the length of the subStr
        }
        //Appends the character at index i of mainStr to newStr
        newStr += mainStr[i];
    }

    //Returns newStr
    return newStr;
}
//}
