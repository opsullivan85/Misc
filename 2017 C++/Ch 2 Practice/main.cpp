// Chapter 2 Practice

#include <iostream>

using namespace std;

int main()
{

    //5. Average of Values
    cout << "5. Average of Values" << endl;
    int var1 = 28, var2 = 32, var3 = 37, var4 = 24, var5 = 33;
    int sum = var1 + var2 + var3 + var4 + var5;
    double average = sum / 5.0;
    cout << average << endl;
    cout << endl;

    //9. Cyborg Data Type Sizes
    cout << "9. Cyborg Data Type Sizes" << endl;
    cout << "Size of char: " << sizeof(char) << " Bytes" << endl;
    cout << "Size of int: " << sizeof(int) << " Bytes" << endl;
    cout << "Size of float: " << sizeof(float) << " Bytes" << endl;
    cout << "Size of double: " << sizeof(double) << " Bytes" << endl;
    cout << endl;

    //13. Circuit Board Price
    cout << "13. Circuit Board Price" << endl;
    double profit = 0.4;
    double cost = 12.67;
    double markup = cost * (profit + 1);
    cout << "The selling price of a $" << cost << " circuit board is: $" << markup << endl;
    cout << endl;

    return 0;
}
