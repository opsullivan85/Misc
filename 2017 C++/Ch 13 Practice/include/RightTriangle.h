#ifndef RIGHTTRIANGLE_H
#define RIGHTTRIANGLE_H


class RightTriangle{
    private:
        double height;
        double width;
        double hypotenuse;
        double longestSide();
        double shortestSide();

    public:
        RightTriangle();
        ~RightTriangle();
        void setSideLengths(double, double, double);
        void makeRight();
        double getHeight() const;
        double getWidth() const;
        double getHypotenuse() const;
        double getArea() const;
        double getPerimeter() const;
        bool isRightTriangle() const;
};

#endif // RIGHTTRIANGLE_H
