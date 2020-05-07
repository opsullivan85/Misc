//Chapter 4 Practice

#include <iostream>
#include <iomanip>
#include <cstdlib>

void daysInMonth();
void mathTutor();
void bankCharges();
void personalBest();
void speedOfSound();

using namespace std;

int main(){
    cout << setprecision(1) << left<< fixed;
    daysInMonth();
    mathTutor();
    bankCharges();
    personalBest();
    speedOfSound();
}

void daysInMonth(){
    //10. Days in a Month
    int month, year;
    cout << "10. Days in a Month" << endl;
    cout << "Enter a month(1-12): ";
    cin >> month;
    cout << "Enter a year: ";
    cin >> year;
    switch(month){
        case 2:
            if((year % 400 == 0 || year % 100 != 0 && year % 4 == 0) && month == 2)
                cout << "29 days";
            else
                cout << "28 days";
            break;
        case 4:
            cout << "30 days";
            break;
        case 6:
            cout << "30 days";
            break;
        case 9:
            cout << "30 days";
            break;
        case 11:
            cout << "30 days";
            break;
        default: cout << "31 days";
    }
    cout << endl;
}

void mathTutor(){
    //11. Math Tutor
    cout << "11. Math Tutor" << endl;
    srand(time(NULL));
    int num1, num2, maxVal = 999, minVal = 0, answer, guess;
    num1 = (rand() % (maxVal - minVal + 1)) - minVal;
    num2 = (rand() % (maxVal - minVal + 1)) - minVal;
    answer = num1 + num2;
    cout << setprecision(1) << fixed << right;
    cout << setw(5) << num1 << endl << "+" << setw(4) << num2 << endl << "-------" << endl;
    cin >> guess;
    answer == guess ? cout << "Correct" : cout << "Incorrect, the answer was " << answer << endl;
    cout << endl;
}

void bankCharges(){
    //14. Bank Charges
    const double BASE_CHARGE = 10.0, LOW_BAL_NUM = 400, LOW_BAL_FEE = 15;
    const double LOW_FEE = 0.1, MED_FEE = 0.08, HIG_FEE = 0.06, HIGHEST_FEE = 0.04, LOW_CHECKS = 20, MED_CHECKS = 40, HIG_CHECKS = 60;
    cout << "14. Bank Charges" << endl;
    int checks;
    double bal, fee, charges = BASE_CHARGE;
    cout << "Balance: ";
    cin >> bal;
    cout << "Checks: ";
    cin >> checks;
    while(checks < 0){
        cout << "Checks can only be positive\n" << "Checks: ";
        cin >> checks;
    }
    if(checks < LOW_CHECKS)
        fee = LOW_FEE;
    else if(checks < MED_CHECKS)
        fee = MED_FEE;
    else if(checks < HIG_CHECKS)
        fee = HIG_FEE;
    else
        fee = HIGHEST_FEE;
    charges += fee * checks;
    if(bal < LOW_BAL_NUM)
        charges += LOW_BAL_FEE;
    if(bal < 0)
        cout << "YOU HAVE OVERDRAWN!\n";
    cout << setprecision(2);
    cout << "You owe the bank $" << charges << " in fees this month.\n";
    cout << endl;
    cin.ignore();
}

void personalBest(){
    //17. Personal Best
    cout << "17. Personal Best" << endl;
    string p1, p2, p3, first, second, third;
    double t1, t2, t3;
    cout << "Person 1: ";
    getline(cin, p1);
    cout << "Person 2: ";
    getline(cin, p2);
    cout << "Person 3: ";
    getline(cin, p3);
    cout << p1 << "'s time:";
    cin >> t1;
    cout << p2 << "'s time:";
    cin >> t2;
    cout << p3 << "'s time:";
    cin >> t3;
    if(t1 > t2 && t2 > t3 && t1 > t3){
        first = p3;
        second = p2;
        third = p1;
    } else if(t1 > t2 && t2 < t3 && t1 > t3){
        first = p2;
        second = p3;
        third = p1;
    } else if(t1 < t2 && t2 > t3 && t1 > t3){
        first = p3;
        second = p1;
        third = p2;
    } else if(t1 < t2 && t2 > t3 && t1 < t3){
        first = p1;
        second = p3;
        third = p2;
    } else if(t1 > t2 && t2 < t3 && t1 < t3){
        first = p2;
        second = p1;
        third = p3;
    } else if(t1 < t2 && t2 < t3 && t1 < t3){
        first = p1;
        second = p2;
        third = p3;
    }
    cout << "Their rankings are as follows (first-last)\n";
    cout << first << " " << second << " " << third << endl;
    cout << endl;
}

void speedOfSound(){
    //20. The Speed of Sound
    cout << "20. The Speed of Sound" << endl;
    const int AIR_SPEED = 1100;
    const int WATER_SPEED = 4900;
    const int STEEL_SPEED = 16400;
    int selection, distance;
    double speed;
    do{
        cout << "Select One: Air(0), Water(1), Steel(2): ";
        cin >> selection;
        cout << "What distance shall the sound wave travel?: ";
        cin >> distance;
        if(distance < 0 || distance > 2)
            cout << "Please input a valid number.";
    }while(distance < 0 || distance > 2);
    switch(selection){
        case 0: speed = AIR_SPEED;
                break;
        case 1: speed = WATER_SPEED;
                break;
        case 2: speed = STEEL_SPEED;
                break;
    }
    cout << setprecision(4) << "That would take " << distance / speed << "s\n";
    cout << endl;
}
