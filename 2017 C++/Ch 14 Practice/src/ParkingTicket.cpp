#include "ParkingTicket.h"
#include "ParkedCar.h"
#include "PoliceOfficer.h"

ParkingTicket::ParkingTicket(){
    fine = 0.0;
}

ParkingTicket::~ParkingTicket(){
    //dtor
}

void ParkingTicket::setParkedCar(ParkedCar car){
    this.car = car;
}

void ParkingTicket::setPoliceOfficer(PoliceOfficer officer){
    this.officer = officer;
}

void ParkingTicket::setHoursIllegalyParked(int hours){
    if(hours > 0){
        hours--;
        fine += 25;
    }
    while(hours > 0){
        hours--;
        fine += 10;
    }
}

ParkedCar car;
//set car
PoliceOfficer officer;
//set officer
ParkingMeter meter;
//set meter
if(officer.examine(car, meter)){
    ParkingTicket ticket = officer.makeTicket(car, hours);
}
