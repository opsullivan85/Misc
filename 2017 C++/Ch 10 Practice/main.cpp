//Chapter 10 practice

//{ Includes
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <cctype>
//}

//{ Namespace
using namespace std;
//}

//{ Function Prototypes
void passwordVerifier();
  bool meetsCriteria(string);
//}

int main(){
    cout << setprecision(1) << left << fixed;
    passwordVerifier();
}

//{ 12. Password Verifier
//Practice:
void passwordVerifier(){
    bool goodPWD;
    string pwd;
    cout << "12. Password Verifier" << endl;
    do{
        cout << "  Please enter a strong password: ";
        getline(cin, pwd);
        goodPWD = meetsCriteria(pwd);
    } while(!goodPWD);
    cout << "Password confirmed\n";
    cout << endl;
}

bool meetsCriteria(string pwd){
    bool eightLong = false;
    bool oneUpper = false;
    bool oneLower = false;
    bool oneDigit = false;
    int len = pwd.length();
    char car;
    if(len > 8)
        eightLong = true;
    for(int c = 0; c < len; c++){
        car = pwd[c];
        if(isupper(car))
            oneUpper = true;
        if(islower(car))
            oneLower = true;
        if(isdigit(car))
            oneDigit = true;
    }
    if(!eightLong || !oneUpper || !oneLower || !oneDigit){
        cout << "  Weak password. Your password needs at least:\n";
        if(!eightLong)
            cout << "    * 8 characters\n";
        if(!oneUpper)
            cout << "    * 1 uppercase letter\n";
        if(!oneLower)
            cout << "    * 1 lowercase letter\n";
        if(!oneDigit)
            cout << "    * 1 digit\n";
    }
    return (eightLong && oneUpper && oneLower && oneDigit);
}
//}
