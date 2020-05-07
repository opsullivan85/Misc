//Chapter 5 practice

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>

void hotelOccupancy();
void studentGrades();
void saveFriends();
void readFriends();

using namespace std;

int main(){
    cout << setprecision(1) << left << fixed;
    hotelOccupancy();
    studentGrades();
    saveFriends();
    readFriends();
}

void hotelOccupancy(){
    //8. Hotel Occupancy
    //Practice: constants, do-while, sentinel, switch
    cout << "8. Hotel Occupancy" << endl;
    int floors, roomsTotal = 0, roomsOnFloor, fullTotal = 0, fullOnFloor;
    cout << "How many floors?: ";
    cin >> floors;
    while(floors < 1){
        cout << "Floors must be > 0\n";
        cout << "How many floors?: ";
        cin >> floors;
    }
    for(int f = 1; f <= floors; f++){
        if(f != 13){
            cout << "Rooms on floor #" << f << " : ";
            cin >> roomsOnFloor;
            while(roomsOnFloor < 10){
            cout << "Rooms must be > 9\n";
            cout << "Rooms on floor #" << f << " : ";
            cin >> roomsOnFloor;
            }
            roomsTotal += roomsOnFloor;
            cout << "How many rooms are full on floor #" << f << "?: ";
            cin >> fullOnFloor;
            while(fullOnFloor > roomsOnFloor){
                cout << "This cannot be greater than the rooms per floor\n";
                cout << "How many rooms are full on floor #" << f << "?: ";
                cin >> fullOnFloor;
            }
            fullTotal += fullOnFloor;
        }
    }
    cout << "Total rooms: " << roomsTotal << endl;
    cout << "Unoccupied: " << roomsTotal - fullTotal << endl;
    cout << "Occupied: " << fullTotal << endl;
    cout << "Percent occupied: " << setprecision(0) << fullTotal * 100.0 / roomsTotal << "%\n";
    cout << endl;
}

void studentGrades(){
    //14. Student Grades
    //Practice: nested for loops
    cout << "14. Student Grades" << endl;
    int students, numTests;
    double studentAvg, score;
    cout << "# of students: ";
    cin >> students;
    cout << "Tests per student: ";
    cin >> numTests;
    for(int s = 1; s <= students; s++){
        studentAvg = 0.0;
        cout << "Student #" << s << endl;
        for(int t = 1; t <= numTests; t++){
            cout << "    Score for test #" << t << ": ";
            cin >> score;
            studentAvg += score;
        }
        studentAvg /= numTests;
        cout << "    Student #" << s << "'s average score is: " << studentAvg << "%.\n";
    }
    cout << endl;
}

void saveFriends(){
    //18. Save Friends List
    //Practice: file output
    cout << "18. Save Friends List" << endl;
    string fileName, f1, f2, f3;
    ofstream outfile;
    cout << "Output filename: ";
    cin >> fileName;
    cout << "Friend 1: ";
    cin.ignore();
    getline(cin, f1);
    cout << "Friend 2: ";
    getline(cin, f2);
    cout << "Friend 3: ";
    getline(cin, f3);
    outfile.open(fileName);
    outfile << f1 << endl << f2 << endl << f3 << endl;
    outfile.close();
    cout << endl;
}

void readFriends(){
    //19. Read Friends List File
    //Practice: file input
    cout << "19. Read Friends List File" << endl;
    string fileName, friendname;
    ifstream infile;
    cout << "File name: ";
    cin >> fileName;
    infile.open(fileName);
    while(infile){
        getline(infile, friendname);
        cout << friendname << endl;
    }
    infile.close();
    cout << endl;
}
