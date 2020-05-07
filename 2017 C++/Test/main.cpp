//Test

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;
void getPrimes(int);


int main(){
    getPrimes(1000);
}

void getPrimes(int num){
    int* primes = new int[num];
    for(int i = num; i >= 1; i--){
        primes[i] = i;
    }

    for(int i = 0; i >= num; i--){
        cout << primes[i];
    }
}
