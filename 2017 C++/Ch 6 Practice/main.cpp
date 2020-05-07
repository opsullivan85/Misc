//Chapter 6 practice

//{ Includes
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
//}

//{ Function Prototypes
void starSearch();
  void getJudgeData(double&, int);
  void calcScore(double, double, double, double, double);
    double findLowest(double, double, double, double, double);
    double findHighest(double, double, double, double, double);
void overloadedHospital();
  double charges(int, double, double, double);
  double charges(double, double);
void paintJobEstimator();
void rpsGame();
  int cpuMove();
  int userMove();
  int findWinner(int, int);
//}

//{ Namespace
using namespace std;
//}

int main(){
    cout << setprecision(1) << left << fixed;
    starSearch();
    overloadedHospital();
    paintJobEstimator();
    rpsGame();
}

//{ 12. Star Search
//Practice:
void starSearch(){
    cout << "12. Star Search" << endl;
    double j1, j2, j3, j4, j5;
    getJudgeData(j1, 1);
    getJudgeData(j2, 2);
    getJudgeData(j3, 3);
    getJudgeData(j4, 4);
    getJudgeData(j5, 5);
    calcScore(j1, j2, j3, j4, j5);
    cout << endl;
}

void getJudgeData(double& j, int n){
    cout << "Judge " << n << "'s score: ";
    cin >> j;
    while(j < 0 || j > 10){
        cout << "Judge " << n << "'s score (0-10): ";
        cin >> j;
    }
}

void calcScore(double j1, double j2, double j3, double j4, double j5){
    double lowest = findLowest(j1, j2, j3, j4, j5);
    double highest = findHighest(j1, j2, j3, j4, j5);
    double score = (j1 + j2 + j3 + j4 + j5 - lowest - highest) / 3;
    cout << "The performers score is " << score << endl;
}

double findLowest(double j1, double j2, double j3, double j4, double j5){
    double lowest = j1;
    if(lowest > j2)
        lowest = j2;
    if(lowest > j3)
        lowest = j3;
    if(lowest > j4)
        lowest = j4;
    if(lowest > j5)
        lowest = j5;
    return lowest;
}

double findHighest(double j1, double j2, double j3, double j4, double j5){
    double highest = j1;
    if(highest < j2)
        highest = j2;
    if(highest < j3)
        highest = j3;
    if(highest < j4)
        highest = j4;
    if(highest < j5)
        highest = j5;
    return highest;
}
//}

//{ 14. Overloaded Hospital
//Practice: overloaded functions, function prototypes
void overloadedHospital(){
    cout << "14. Overloaded Hospital" << endl;
    double services, meds, charge;
    int status;
    do{
        cout << "In-patient(0) or Out-patient(1): ";
        cin >> status;
    } while(status < 0 || status > 1);

    do{
        cout << "Charges for services: ";
        cin >> services;
    } while(services < 0);
    do{
        cout << "Charges for medications: ";
        cin >> meds;
    } while(meds < 0);

    if(status == 0){
        int days;
        double rate;
        do{
            cout << "Days in hospital: ";
            cin >> days;
        } while(days < 0);
        do{
            cout << "Daily rate: ";
            cin >> rate;
        } while(rate < 0);
        charge = charges(days, rate, meds, services);
    } else {
        charge = charges(meds, services);
    }
    cout << "Total charges = $" << setprecision(2) << charge << endl;
    cout << endl;
}

double charges(int days, double rate, double meds, double services){
    return (rate * days + meds + services);
}

double charges(double meds, double services){
    return (meds + services);
}
//}

//{ 17. Paint Job Estimator
//Practice: constants, function prototypes, comment each function, formatted output
void paintJobEstimator(){
    cout << "17. Paint Job Estimator" << endl;
    int rooms, sqft, temp;
    double ppgal;
    do{
        cout << "How many rooms?: ";
        cin >> rooms;
    } while (rooms < 1);
    for(int room = 1; room <= rooms; room++){
        do{
            cout << "SQFT of wall space in room #" << room << ": ";
            cin >> temp;
        } while(temp < 0);
        sqft += temp;
    }
    do{
        cout << "$/gal of paint: ";
        cin >> ppgal;
    } while(ppgal < 10);
    cout << sqft / 110.0 << " gallons of paint required\n";
    cout << 8.0 * sqft / 110.0 << " hours of labor required\n";
    cout << "$" << setprecision(2) << ppgal * sqft / 110.0 << " in paint needed\n";
    cout << "$" << setprecision(2) << 25.00 * 8.0 * sqft / 110.0 << " in labor costs\n";
    cout << "$" << setprecision(2) << (25.00 * 8.0 * sqft / 110.0) + (ppgal * sqft / 110.0) << " total costs\n";
    cout << endl;
}
//}

//{ 23. Rock, Paper, Scissors Game
//Practice: use constants for rock, paper, scissors
void rpsGame(){
    cout << "23. Rock, Paper, Scissors Game" << endl;
    int cpu, user, winner, cpuScore = 0, userScore = 0;
    const int r = 1, p = 2, s = 3;
    bool replay;
    do{
        do{
            cpu = cpuMove();
            user = userMove();
            if(cpu == r){
                cout << "The computer chose rock\n";
            } else if(cpu = p){
                cout << "The computer chose paper\n";
            } else{
                cout << "The computer chose scissors\n";
            }
            winner = findWinner(cpu, user);
            if(winner == 1)
                userScore++;
            else if(winner == -1)
                cpuScore++;
        } while(winner == 0);
        cout << "Computer " << cpuScore << " : You " << userScore << endl << endl;
        cout << "Replay?: No(0) / Yes(1): ";
        cin >> replay;
    } while(replay);
    cout << endl;
}

int cpuMove(){
    srand(time(NULL));
    return (rand() % 3 + 1);
}

int userMove(){
    int choice;
    do{
        cout << "Pick one: Rock(1), Paper(2), Scissors(3): ";
        cin >> choice;
    } while(choice < 1 || choice > 3);
    return choice;
}

int findWinner(int cpu, int user){
        if(user - 1 == cpu || user + 2 == cpu){
            cout << "You beat the computer!\n";
            return 1;
        } else if(user + 1 == cpu || user - 2 == cpu){
            cout << "The computer beat you!\n";
            return -1;
        } else{
            cout << "You tied, go again.\n";
            return 0;
        }
}
//}
