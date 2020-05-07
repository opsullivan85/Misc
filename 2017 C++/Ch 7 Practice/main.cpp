//Chapter 7 practice

//{ Includes
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
//}

//{ Function Prototypes
void chipsAndSalsa();
void lotteryApplication();
  void printIntArray(int[], int);
void ticTacToe();
  const int TIE = -1, NONE = 0, P1_VIC = 1, P2_VIC = 2;
  void clrBoard(char[][3]);
  void dispBoard(char[][3]);
  void playerMove(char[][3], int, char);
  int getGameStatus(char[][3], char[]);
void twoDimentionalArrayOperations();
  const int ARRAY_COLS = 3;
  const int ARRAY_ROWS = 3;
  void arryFillRandInt(int[][ARRAY_COLS]);
  void print2DIntArray(int[][ARRAY_COLS]);
  int getTotal(int[][ARRAY_COLS], int[][ARRAY_COLS]);
  double getAverage(int[][ARRAY_COLS]);
  int getRowTotal(int[][ARRAY_COLS], int);
  int getColumnTotal(int[][ARRAY_COLS], int);
  int getHighestInRow(int[][ARRAY_COLS], int);
  int getLowestInRow(int[][ARRAY_COLS], int);
//}

//{ Namespace
using namespace std;
//}

int main(){
    cout << setprecision(1) << left << fixed;
    //chipsAndSalsa();
    //lotteryApplication();
    ticTacToe();
    //twoDimentionalArrayOperations();
}

//{ 3. Chips and Salsa
//Practice:
void chipsAndSalsa(){
    cout << "3. Chips and Salsa" << endl;
    const int SIZE = 5;
    string name[] = {"mild", "medium", "sweet", "hot", "zesty"};
    int numSold[SIZE];
    int low = 0, high = 0, total = 0;
    for(int i = 0; i < SIZE; i++){
        cout << "Sales of the " << name[i] << " salsa: ";
        cin >> numSold[i];
        while(numSold[i] < 0){
            cout << "Please input a POSITIVE value: ";
            cin >> numSold[i];
        }
        total += numSold[i];
    }
    for(int i = 1; i < SIZE; i++){
        if(numSold[low] > numSold[i])
            low = i;
        if(numSold[high] < numSold[i])
            high = i;
    }
    for(int i = 0; i < SIZE; i++){
        cout << "The " << name[i] << " salsa had " << numSold[i] << " sales.\n";
    }
    cout << "There were " << total << " total sales.\n";
    cout << "The worst selling salsa was " << name[low] << ".\n";
    cout << "The best selling salsa was " << name[high] << ".\n";
    cout << endl;
}
//}

//{ 14. Lottery Application
//Practice:
void lotteryApplication(){
    const int LEN = 5;
    int answer[LEN], guess[LEN], numCorrect = 0;
    cout << "14. Lottery Application" << endl;
    cout << "Enter " << LEN << " lottery numbers (0-9, separated by spaces): ";
    for(int i = 0; i < LEN; i++){
        cin >> guess[i];
        answer[i] = rand() % 10;
        answer[i] == guess[i] ? numCorrect += 1 : numCorrect += 0;
    }
    cout << "The correct answer was: ";
    printIntArray(answer, LEN);
    cout << "You got " << numCorrect << " number(s) correct.\n";
    if(numCorrect == LEN)
        cout << "You won the jackpot!\n";
    cout << endl;
}

void printIntArray(int intArray[], int len){
    for(int i = 0; i < len; i++)
        cout << intArray[i] << " ";
    cout << endl;
}
//}

//{ 18. Tic-Tac-Toe Game
//Practice:
void ticTacToe(){
    cout << "18. Tic-Tac-Toe Game" << endl;

    //Initialize values for game states
    const int TIE = -1, NONE = 0, P1_VIC = 1, P2_VIC = 2;

    //Initialization
    char plrSym[2] = {'X', 'O'};
    char board[3][3];
    int status = 0;
    bool replay;

    //Keeps playing games while player wants to
    do{
        clrBoard(board);
        do{
            for(int p = 1; p  <= 2; p++){
                status = getGameStatus(board, plrSym);

                //Prompts player move if there is no game state
                if(status == NONE){
                    dispBoard(board);
                    playerMove(board, p, plrSym[p-1]);
                }
            }
        } while(NONE == status);

        //Displays game state
        if(status == TIE){
            cout << "The game was a tie!\n";
        } else if(status == P1_VIC){
            cout << "Player #1 won!\n";
        } else if(status == P2_VIC){
            cout << "Player # 2 won!\n";
        }

        cout << "Replay? Yes(1)/No(0): ";
        cin >> replay;
    } while(replay);

    cout << endl;
}

//Fills passes array with * chars
void clrBoard(char board[][3]){
    for(int r = 0; r < 3; r++){
        for(int c = 0; c < 3; c++){
            board[r][c] = '*';
        }
    }
}

//Prints out passes array
void dispBoard(char board[][3]){
    for(int r = 0; r < 3; r++){
        for(int c = 0; c < 3; c++){
            cout << board[r][c] << " ";
        }
        cout << endl;
    }
}

//Prompts for player move given board, player number and player symbol
void playerMove(char board[][3], int plrNum, char plrSym){
    int row, col;

    cout << "Player #" << plrNum << " (" << plrSym << "):\n";
    do{
        do{
            cout << "  Col(1-3): ";
            cin >> col;
            col--;
        } while(col < 0 || col > 2);

        do{
            cout << "  Row(1-3): ";
            cin >> row;
            row--;
        } while(row < 0 || row > 2);

        if('*' != board[row][col]){
            cout << "  Please select an empty space.\n";
        }
    } while('*' != board[row][col]);
    board[row][col] = plrSym;
}

//Returns current board state given board and player array
int getGameStatus(char board[][3], char PLR_SYM[]){
    bool playerVict[2] = {false, false};
    bool tie = true, horizontal = true, vertical = true, diagonal = true;

    //Checks which player, if either, won
    for(int p = 0; p < 2; p++){
        for(int r = 0; r < 3; r++){
            for(int c = 0; c < 3; c++){
                if(board[r][c] != PLR_SYM[p]){
                    horizontal = false;
                }
            }

            if(board[2-r][r] != PLR_SYM[p]){
                diagonal = false;
            }

            if(horizontal){
                playerVict[p] = true;
            }
            horizontal = true;
        }

        if(diagonal){
            playerVict[p] = true;
        }
        diagonal = true;

        for(int c = 0; c < 3; c++){
            for(int r = 0; r < 3; r++){
                if(board[r][c] != PLR_SYM[p]){
                    vertical = false;
                }
            }

            if(board[c][c] != PLR_SYM[p]){
                diagonal = false;
            }

            if(vertical){
                playerVict[p] = true;
            }
            vertical = true;
        }

        if(diagonal){
            playerVict[p] = true;
        }
        diagonal = true;
    }

    //Checks for tie game
    for(int r = 0; r < 3; r++){
        for(int c = 0; c < 3; c++){
            if('*' == board[r][c]){
                tie = false;
            }
        }
    }

    //Returns board state
    if(playerVict[0]){
        return P1_VIC;
    } else if(playerVict[1]){
        return P2_VIC;
    } else if(tie){
        return TIE;
    } else{
        return NONE;
    }
}
//}

//{ 19. 2D Array Operations
//Practice:
void twoDimentionalArrayOperations(){
    cout << "19. 2D Array Operations" << endl;

    //Initialization
    int array1[ARRAY_ROWS][ARRAY_COLS], array2[ARRAY_ROWS][ARRAY_COLS], rowToTotal, colToTotal, row;

    //Filling arrays with random digits
    arryFillRandInt(array1);
    arryFillRandInt(array2);

    //Displays each array
    cout << "Array 1" << endl;
    print2DIntArray(array1);
    cout << "Array 2" << endl;
    print2DIntArray(array2);

    //Displays array 1 and array 2 total and array 1 average
    cout << "  Total = " << getTotal(array1, array2) << endl;
    cout << "  Average = " << getAverage(array1) << endl;

    //Prompts for row to total and displays total of row
    do{
        cout << "  Row to total: ";
        cin >> rowToTotal;
    } while(rowToTotal < 0 || rowToTotal >= ARRAY_ROWS);
    cout << "    Row total = " << getRowTotal(array1, rowToTotal) << endl;

    //Prompts for column to total and displays total of row
    do{
        cout << "  Col to total: ";
        cin >> colToTotal;
    } while(colToTotal < 0 || colToTotal >= ARRAY_COLS);
    cout << "    Col total = " << getColumnTotal(array1, colToTotal) << endl;

    //Prompts user for row and displays the highest and lowest in row
    do{
        cout << "  Row: ";
        cin >> row;
    } while(row < 0 || row >= ARRAY_ROWS);
    cout << "    Row max = " << getHighestInRow(array1, row) << endl;
    cout << "    Row min = " << getHighestInRow(array1, row) << endl;
    cout << endl;
}

//Fills the passed array with random digits
void arryFillRandInt(int arry[][ARRAY_COLS]){
    srand(time(0));
    for(int r = 0; r < ARRAY_ROWS; r++){
        for(int c = 0; c < ARRAY_COLS; c++){
            arry[r][c] = rand() % 10;
        }
    }
}

//Prints out the passed array
void print2DIntArray(int arry[][ARRAY_COLS]){
    for(int r = 0; r < ARRAY_ROWS; r++){
        for(int c = 0; c < ARRAY_COLS; c++){
            cout << arry[r][c] << " ";
        }
        cout << endl;
    }
}

//Returns the total of the 2 passed arrays
int getTotal(int arry1[][ARRAY_COLS], int arry2[][ARRAY_COLS]){
    int total = 0;
    for(int r = 0; r < ARRAY_ROWS; r++){
        for(int c = 0; c < ARRAY_COLS; c++){
            total += arry1[r][c] + arry2[r][c];
        }
    }
    return total;
}

//Returns the average of the passed array
double getAverage(int arry[][ARRAY_COLS]){
    double avg = 0;
    for(int r = 0; r < ARRAY_ROWS; r++){
        for(int c = 0; c < ARRAY_COLS; c++){
            avg += arry[r][c];
        }
    }
    return avg / (ARRAY_ROWS * ARRAY_COLS);
}

//Returns the total of the passed row of the passed array
int getRowTotal(int arry[][ARRAY_COLS], int rowToTotal){
    int total = 0;
    for(int c = 0; c < ARRAY_COLS; c++){
        total += arry[rowToTotal][c];
    }
    return total;
}

//Returns the total of the passed column of the passed array
int getColumnTotal(int arry[][ARRAY_COLS], int collumnToTotal){
    int total = 0;
    for(int r = 0; r < ARRAY_ROWS; r++){
        total += arry[r][collumnToTotal];
    }
    return total;
}

//Returns highest number in the passed row of the passed array
int getHighestInRow(int arry[][ARRAY_COLS], int rowNum){
    int highest = 0;
    for(int c = 0; c < ARRAY_COLS; c++){
        if(arry[rowNum][c])
            highest = arry[rowNum][c];
    }
    return highest;
}

//Returns lowest number in the passed row of the passed array
int getLowestInRow(int arry[][ARRAY_COLS], int rowNum){
    int lowest = 0;
    for(int c = 0; c < ARRAY_COLS; c++){
        if(arry[rowNum][c])
            lowest = arry[rowNum][c];
    }
    return lowest;
}
//}
