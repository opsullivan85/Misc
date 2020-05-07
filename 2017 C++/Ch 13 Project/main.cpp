//Owen Sullivan 5/30
//Chapter 13 project

//{ Includes
#include "Coin.h"
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <cctype>
#include <cstring>

#include <string>
#include <ctime>
//}

//{ Namespace
using namespace std;
//}

//{ Function Prototypes
void coinTossSimulator();
void coinTossForADolar();
//}

int main(){
    cout << setprecision(2) << left << fixed;
    coinTossSimulator();
    coinTossForADolar();
}

//{ 12. Coin Toss Simulator
//This function has no parameters or returns
//It simulates flipping 20 coins and shows the results
void coinTossSimulator(){
    //Initialization
    const int TOSSES = 20;
    int heads = 0, tails = 0;
    Coin coin;

    cout << "12. Coin Toss Simulator" << endl;
    cout << "  The coin started on: " << coin.getSideUp() << endl;

    for(int i = 1; i <= TOSSES; i++){
        //Tosses the coin
        coin.toss();
        //Displays the result of the toss
        cout << "  Toss " << i << ": " << coin.getSideUp() << endl;
        //Increments either heads or tails based on the toss
        (coin.getSideUp() == "heads") ? (heads++) : (tails++);
    }

    //Displays the head / tail count
    cout << "  You got " << heads << " heads\n";
    cout << "  You got " << tails << " tails\n";

    cout << endl;
}
//}

//{ 13. Tossing Coin for a Dollar
//This function has no parameters or returns
//It plays a game - three coins are thrown,
// if one lands on heads its value is added to the balance.
// The goal it to hit $1.00 exactly.
void coinTossForADolar(){
    //Initialization
    const double WIN_AMMOUNT = 1.00,
                 QUARTER_VAL = 0.25,
                 DIME_VAL = 0.10,
                 NICKLE_VAL = 0.05;
    double bal = 0.00, gained = 0.00;
    Coin quarter, dime, nickel;

    cout << "13. Tossing Coin for a Dollar" << endl;

    //Waits for "Valuable" user input
    cout << "  Shall we play a game?: ";
    //This flushes everything in the cin buffer upto the next '\n'
    cin.ignore(INT_MAX, '\n');

    while(bal < WIN_AMMOUNT){

        //Flips the quarter, shows side up and any added balance
        quarter.toss();
        gained = (quarter.getSideUp() == "heads") * QUARTER_VAL;
        bal += gained;
        cout << setw(15) << "  Quarter: " << quarter.getSideUp();
        cout << " (+$" << gained << ")\n";

        //Flips the dime, shows side up and any added balance
        dime.toss();
        gained = (dime.getSideUp() == "heads") * DIME_VAL;
        bal += gained;
        cout << setw(15) << "  Dime: " << dime.getSideUp();
        cout << " (+$" << gained << ")\n";

        //Flips the nickel, shows side up and any added balance
        nickel.toss();
        gained = (nickel.getSideUp() == "heads") * NICKLE_VAL;
        bal += gained;
        cout << setw(15) << "  Nickel: " << nickel.getSideUp();
        cout << " (+$" << gained << ")\n";

        //Displays balance then waits for user acknowledgment
        cout << setw(23) << "  Balance:" << "$" << bal << endl;
        cout << "  Press (Enter)...";
        cin.ignore(INT_MAX, '\n');
        cout << endl;
    }

    if(bal == WIN_AMMOUNT)
        cout << "  Congratulations, you won!";
    else
        cout << "  Sorry, you lost.";
    cout << endl;
}
//}
