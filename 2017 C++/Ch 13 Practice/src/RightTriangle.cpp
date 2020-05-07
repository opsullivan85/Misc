//{ RightTriangle
#include "RightTriangle.h"
#include <cmath>

//{ private
double RightTriangle::longestSide(){
    double longest = height;
    if(longest < width)
        longest = width;
    if(longest < hypotenuse)
        longest = hypotenuse;
    return longest;
}

double RightTriangle::shortestSide(){
    double shortest = height;
    if(shortest > width)
        shortest = width;
    if(shortest > hypotenuse)
        shortest = hypotenuse;
    return shortest;
}
//}

//{ public
RightTriangle::RightTriangle(){
    height = 0.0;
    width = 0.0;
    hypotenuse = 0.0;
}

RightTriangle::~RightTriangle(){

}

void RightTriangle::setSideLengths(double a, double b, double c){
    height = a;
    width = b;
    hypotenuse = c;
}

void RightTriangle::makeRight(){
    double longest = longestSide();
    double shortest = shortestSide();
    height = shortest;
    hypotenuse = longest;
    width = sqrt(hypotenuse * hypotenuse - height * height);
}

double RightTriangle::getHeight() const{
    return height;
}

double RightTriangle::getWidth() const{
    return width;
}

double RightTriangle::getHypotenuse() const{
    return hypotenuse;
}

double RightTriangle::getArea() const{
    return (0.5 * height * width);
}

double RightTriangle::getPerimeter() const{
    return (height + width + hypotenuse);
}

bool RightTriangle::isRightTriangle() const{
    return (height * height + width * width == hypotenuse * hypotenuse);
}
//}
//}
