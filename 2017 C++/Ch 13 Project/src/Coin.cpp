#include "Coin.h"
#include <cstdlib>
#include <ctime>

using namespace std;

//Constructor
Coin::Coin(){
    //Sets random seed
    srand(time(0));

    //Tosses the coin to randomize side up
    toss();
}

//Randomizes the side up
void Coin::toss(){
    (rand() % 2) ? (sideUp = "heads") : (sideUp = "tails");
}

//Returns the side currently up
string Coin::getSideUp() const{
    return sideUp;
}
