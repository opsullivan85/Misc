#include <iostream>

using namespace std;

#ifndef COIN_H
#define COIN_H

class Coin
{
    private:
        //Stores side currently up
        string sideUp;
    public:
        //Constructor
        Coin();

        //"Tosses" the coin (randomizes side up)
        void toss();

        //Returns the side up
        string getSideUp() const;

};

#endif // COIN_H
