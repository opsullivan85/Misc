// Chapter 3 Practice

#include <iostream>
#include <iomanip>
#include <cstdlib>

using namespace std;

int main()
{

    //7. Box Office
    string movie;
    int adult, child;
    float gross, net, paid;
    cout << "7. Box Office" << endl;

    cout << "What was the movie played? ";
    getline(cin, movie);
    cout << "Adult tickets sold? ";
    cin >> adult;
    cout << "Child tickets sold? ";
    cin >> child;

    gross = adult * 10 + child * 6;
    net = 0.2 * gross;
    paid = gross - net;

    cout << setprecision(2) << fixed << right;
    cout << "Movie Name:                " << setw(10) << movie << endl;
    cout << "Adult Tickets Sold:        " << setw(8) << adult << endl;
    cout << "Child Tickets Sold:        " << setw(8) << child << endl;
    cout << "Gross Box Office Profit:   " << setw(5) << "$" << setw(9) << gross << endl;
    cout << "Net Box Office Profit:     " << setw(5) << "$" << setw(9) << net << endl;
    cout << "Amount Paid to Distributor:" << setw(5) << "$" << setw(9) << paid << endl;
    cout << endl;


    //17. Math Tutor
    char ch;
    int num1 = 247, num2 = 129;
    cout << "17. Math Tutor" << endl;
    cout << setprecision(2) << fixed << right;
    cout << setw(5) << num1 << endl;
    cout  << "+" << setw(4) << num2 << endl;
    cout << "-------";
    cin.ignore().get(ch);
    cout << setw(5) << num1 + num2 << endl;
    cout << endl;


    //20. Pizza Pie
    float pi = 3.14159, diameter, radius;
    cout << setprecision(1) << fixed << right;
    cout << "20. Pizza Pie" << endl;
    cout << "Pizza Diameter: " ;
    cin >> diameter;
    radius = diameter/2;
    cout << "Cut the pizza into " << pi * radius * radius / 14.125 << " pieces." << endl;
    cout << endl;


    //21. How many pizzas?
    float ppl;
    cout << setprecision(1) << fixed << right;
    cout << "21. How many pizzas?" << endl;
    cout << "People Attending: " ;
    cin >> ppl;
    cout << "Pizza Diameter:";
    cin >> diameter;
    cout << "Buy " << ppl * ( 14.125 / pi) << " pizzas." << endl;
    cout << endl;


    //24. Word Game
    string name, city, college, job, animal, pet;
    int age;
    //cout << setprecision(1) << fixed << right;
    cout << "24. Word Game" << endl;
    cin.ignore();
    cout << "Your Name: " ;
    getline(cin, name);
    cout << "Your Age: " ;
    cin >> age;
    cout << "A City: " ;
    cin.ignore();
    getline(cin, city);
    cout << "A College: " ;
    getline(cin, college);
    cout << "A Profession: " ;
    getline(cin, job);
    cout << "An animal: " ;
    getline(cin, animal);
    cout << "A pet name: " ;
    getline(cin, pet);
    cout << "There once was a person named " << name << " who lived in " << city << ". At the age of " << age << ",\n"
        << name << " went to college at " << college << ", " << name << " graduated and went to work as a\n"
        << job << ". Then, " << name << " and adopted a(n) " << animal <<" named " << pet << ". They both\n"
        <<"lived happily ever after.\n";
    cout << endl;
}
