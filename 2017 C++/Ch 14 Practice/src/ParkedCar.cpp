#include "ParkedCar.h"
#include <iostream>

using namespace std;

ParkedCar::ParkedCar()
{
    make = "";
    model = "";
    color = "";
    licenseNumber = "";
    parkMinutes = 0;
}

string ParkedCar::getMake() const { return make; }

string ParkedCar::getModel() const { return model; }

string ParkedCar::getColor() const { return color; }

string ParkedCar::getLicenseNumber() const { return licenseNumber; }

int ParkedCar::getParkMinutes() const { return parkMinutes; }

void ParkedCar::setMake(string m) { make = m; }

void ParkedCar::setModel(string m) { model = m; }

void ParkedCar::setColor(string c) { color = c; }

void ParkedCar::setLicenseNumber(string num) { licenseNumber = num; }

void ParkedCar::setParkMinutes(int minutes) { parkMinutes = minutes; }
