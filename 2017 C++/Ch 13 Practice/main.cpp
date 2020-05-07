//Chapter 13 practice

//{ Includes
#include "RightTriangle.h"
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <fstream>
#include <cctype>
#include <cstring>
#include <string>
//}

//{ Namespace
using namespace std;
//}

//{ Function Prototypes
void RtTriangle();
  void dispTriangleInfo(RightTriangle&);
//}

int main(){
    cout << setprecision(1) << left << fixed;
    RtTriangle();
}

//{ Right Triangle
//Practice:
void RtTriangle(){
    double height, width, hypotenuse;
    cout << "Right Triangle" << endl;
    do{
        cout << "  Height?: ";
        cin >> height;
    } while(height < 0);
    do{
    cout << "  Width?:";
    cin >> width;
    } while(width < 0);
    do{
    cout << "  Hypotenuse?:";
    cin >> hypotenuse;
    } while(hypotenuse < 0);
    RightTriangle triangle;
    triangle.setSideLengths(height, width, hypotenuse);
    if(!triangle.isRightTriangle()){
        cout << "  INVALID: Not a right triangle.\n";
        cout << "  Making a triangle from the longest an shortest side.\n";
        triangle.makeRight();
    }
    dispTriangleInfo(triangle);

    cout << endl;
}

void dispTriangleInfo(RightTriangle &triangle){
    cout << "  Right triangle info:\n";
    cout << "    *Height: " << triangle.getHeight() << endl;
    cout << "    *Width: " << triangle.getWidth() << endl;
    cout << "    *Hypotenuse: " << triangle.getHypotenuse() << endl;
    cout << "    *Area: " << triangle.getArea() << endl;
    cout << "    *Perimeter: " << triangle.getPerimeter() << endl;
}

//}
