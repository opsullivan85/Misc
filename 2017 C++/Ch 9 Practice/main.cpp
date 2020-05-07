//Chapter 9 practice

//{ Includes
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
//}

//{ Namespace
using namespace std;
//}

//{ Function Prototypes
void testScoreNumOne();
  void sortAscendingInt(int*, int);
  double calcAvg(int*, int);
void dropLowestScore();
  void sortAscendingIntDropLowest(int*, int&);
void testScoreNumTwo();
  void sortScoreNamePair(int*, string*, int);
//}

int main(){
    cout << setprecision(1) << left << fixed;
    testScoreNumOne();
    dropLowestScore();
    testScoreNumTwo();
}

//{ 2. Test Scores #1
//Practice:
void testScoreNumOne(){
    double avg;
    int numTests;
    int* scoresIntPtr = nullptr;
    cout << "2. Test Scores #1" << endl;
    do{
        cout << "  How many test scores?: ";
        cin >> numTests;
    } while(numTests < 0);
    scoresIntPtr = new int[numTests];
    for(int t = 0; t < numTests; t++){
        do{
            cout << "    Score #" << t + 1 << ": ";
            cin >> *(scoresIntPtr + t);
        } while(*(scoresIntPtr + t) < 0);
    }
    sortAscendingInt(scoresIntPtr, numTests);
    avg = calcAvg(scoresIntPtr, numTests);
    cout << "  Ranked scores: \n";
    for(int t = 0; t < numTests; t++){
        cout << "    #" << numTests - t << ": " << *(scoresIntPtr + t) << "%\n";
    }
    cout << "  Average score = " << avg  << "%\n";
    delete [] scoresIntPtr;
    cout << endl;
}

void sortAscendingInt(int* intptr, int len){
    int* sortedintptr = new int[len];
    int maxNum = 0, pos = 0;
    for(int i = 0; i < len; i++){
        if(*(intptr + i) > maxNum){
            maxNum = *(intptr + i);
        }
    }
    for(int n = 0; n <= maxNum; n++){
        for(int i = 0; i < len; i++){
            if(*(intptr + i) == n){
                *(sortedintptr + pos) = n;
                *(intptr + i) = -1;
                pos++;
            }
        }
    }
    for(int i = 0; i < len; i++){
        *(intptr + i) = *(sortedintptr + i);
    }
    delete [] sortedintptr;
}

double calcAvg(int* intptr, int len){
    double avg;
    for(int i = 0; i < len; i++){
        avg += *(intptr + i);
    }
    return (avg / len);
}
//}

//{ 3. Drop Lowest Score
//Practice:
void dropLowestScore(){
    double avg;
    int numTests;
    int* scoresIntPtr = nullptr;
    cout << "3. Drop Lowest Score" << endl;
    do{
        cout << "  How many test scores?: ";
        cin >> numTests;
    } while(numTests < 0);
    scoresIntPtr = new int[numTests];
    for(int t = 0; t < numTests; t++){
        do{
            cout << "    Score #" << t + 1 << ": ";
            cin >> *(scoresIntPtr + t);
        } while(*(scoresIntPtr + t) < 0);
    }
    sortAscendingIntDropLowest(scoresIntPtr, numTests);
    avg = calcAvg(scoresIntPtr, numTests - 1);
    cout << "  Ranked scores: \n";
    for(int t = 0; t < numTests; t++){
        cout << "    #" << numTests - t << ": " << *(scoresIntPtr + t) << "%\n";
    }
    cout << "  Average score = " << avg  << "%\n";
    delete [] scoresIntPtr;
    cout << endl;
}

void sortAscendingIntDropLowest(int* intptr, int &len){
    int* sortedintptr = new int[len - 1];
    int maxNum = 0, minNum = *intptr, pos = 0;
    for(int i = 0; i < len; i++){
        if(*(intptr + i) > maxNum){
            maxNum = *(intptr + i);
        }
        if(*(intptr + i) < minNum){
            minNum = *(intptr + i);
            pos = i;
        }
    }
    *(intptr + pos) = -1;
    pos = 0;
    for(int n = 0; n <= maxNum; n++){
        for(int i = 0; i < len; i++){
            if(*(intptr + i) == n){
                *(sortedintptr + pos) = n;
                *(intptr + i) = -1;
                pos++;
            }
        }
    }
    len--;
    delete [] intptr;
    intptr = new int[len];
    for(int i = 0; i < len; i++){
        *(intptr + i) = *(sortedintptr + i);
    }
    delete [] sortedintptr;
}
//}

//{ 4. Test Scores #2
//Practice:
void testScoreNumTwo(){
    double avg;
    int num;
    int* scoresIntPtr = nullptr;
    string* nameStringPtr = nullptr;
    cout << "4. Test Scores #2" << endl;
    do{
        cout << "  How many test scores?: ";
        cin >> num;
    } while(num < 0);
    scoresIntPtr = new int[num];
    nameStringPtr = new string[num];
    for(int t = 0; t < num; t++){
        do{
            cout << "    Score #" << t + 1 << ": ";
            cin >> *(scoresIntPtr + t);
        } while(*(scoresIntPtr + t) < 0);
        cout << "    Student #" << t + 1 << "'s name: ";
        cin.ignore();
        getline(cin, *(nameStringPtr + t));
    }
    sortScoreNamePair(scoresIntPtr, nameStringPtr, num);
    avg = calcAvg(scoresIntPtr, num);
    cout << "  Ranked scores: \n";
    for(int t = 0; t < num; t++){
        cout << "    #" << num - t << ": " << *(nameStringPtr + t)  << " - " << *(scoresIntPtr + t) << "%\n";
    }
    cout << "  Average score = " << avg  << "%\n";
    delete [] scoresIntPtr;
    delete [] nameStringPtr;
    cout << endl;
}

void sortScoreNamePair(int* intptr, string* strptr, int len){
    int* sortedintptr = new int[len];
    string* sortedstrptr = new string[len];
    int maxNum = 0, pos = 0;
    for(int i = 0; i < len; i++){
        if(*(intptr + i) > maxNum){
            maxNum = *(intptr + i);
        }
    }
    for(int n = 0; n <= maxNum; n++){
        for(int i = 0; i < len; i++){
            if(*(intptr + i) == n){
                *(sortedstrptr + pos) = *(strptr + i);
                *(sortedintptr + pos) = *(intptr + i);
                *(intptr + i) = -1;
                pos++;
            }
        }
    }
    for(int i = 0; i < len; i++){
        *(intptr + i) = *(sortedintptr + i);
        *(strptr + i) = *(sortedstrptr + i);
    }
    delete [] sortedintptr;
    delete [] sortedstrptr;
}
//}
