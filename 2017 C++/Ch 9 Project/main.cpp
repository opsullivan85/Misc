//Chapter 9 Project

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
void movieStats();
  void sortArray(int*, int);
  void printArray(int*, int);
  double averageFunction(int*, int);
  int modeFunction(int*, int);
  double medianFunction(int*, int);
//}

int main(){
    cout << setprecision(1) << left << fixed;
    movieStats();
}

//{ 13. Movie Statistics
//Practice:
void movieStats(){

    //Initialization
    int * dataPtr = nullptr;
    int arryLen;

    cout << "13. Movie Statistics" << endl;

    //Gets how many students were surveyed
    do{
        cout << "  How many students were surveyed?: ";
        cin >> arryLen;
    } while(arryLen < 1);

    //Initializes dataPtr to a new array
    dataPtr = new int[arryLen];

    //Inputs data into dataPtr
    for(int i = 0; i < arryLen; i++){
        do{
            cout << "    How many movies did student #" << i + 1 << " see?: ";
            cin >> *(dataPtr + i);
        } while(*(dataPtr + i) < 0);
    }

    //Sorts the data
    sortArray(dataPtr, arryLen);

    //Displays the data statistics
    cout << "  Average: " << averageFunction(dataPtr, arryLen) << endl;
    cout << "  Median: " << medianFunction(dataPtr, arryLen) << endl;
    cout << "  Mode: " << modeFunction(dataPtr, arryLen) << endl;

    cout << endl;
}

/* Prints and integer array
void printArray(int * intPtr, int len){
    for(int i = 0; i < len; i++){
        cout << *(intPtr + i) << " ";
    }
    cout << endl;
}
*/

//Sorts and array low to high given an int pointer and the array length
void sortArray(int * intPtr, int len){
    int tempStorage;
    bool sorted = false;
    while(!sorted){
        sorted = true;
        for(int i = 0; i < len-1; i++){
            if(*(intPtr + i) > *(intPtr + (i + 1))){
                tempStorage = *(intPtr + i);
                *(intPtr + i) = *(intPtr + (i + 1));
                *(intPtr + (i + 1)) = tempStorage;
                sorted = false;
            }
        }
    }
}

//Returns the average of the set given an int pointer and the array length
double averageFunction(int * intPtr, int len){
    double avg;
    for(int i = 0; i < len; i++){
        avg += *(intPtr + i);
    }
    return avg / len;
}

//Returns the mode of the set given an int pointer and the array length
int modeFunction(int * intPtr, int len){
    int * maxPtr = nullptr;
    int maxScore = 1, ocurrences = 1;
    for(int i = 0; i < len; i++){
        if(*(intPtr + i) == *(intPtr + i + 1)){
            ocurrences++;
            if(ocurrences > maxScore){
                maxScore = ocurrences;
                maxPtr = (intPtr + i);
            }
        } else{
            ocurrences = 1;
        }
    }
    if(maxScore == 1){
        return -1;
    } else{
        return *maxPtr;
    }
}

//Returns the median of the set given an int pointer and the array length
double medianFunction(int * intPtr, int len){
    if(len % 2){
        return *(intPtr + (len / 2));
    } else{
        return (*(intPtr + (len / 2) - 1) + *(intPtr + (len / 2))) / 2.0;
    }
}
//}
