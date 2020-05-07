#include <iostream>

using namespace std;

#ifndef PARKEDCAR_H
#define PARKEDCAR_H


class ParkedCar {
    private:
        string make;
        string model;
        string color;
        string licenseNumber;
        int parkMinutes;

    public:
        ParkedCar();
        string getMake() const;
        string getModel() const;
        string getColor() const;
        string getLicenseNumber() const;
        int getParkMinutes() const;
        void setMake(string m);
        void setModel(string m);
        void setColor(string c);
        void setLicenseNumber(string num);
        void setParkMinutes(int minutes);
};

#endif // PARKEDCAR_H
