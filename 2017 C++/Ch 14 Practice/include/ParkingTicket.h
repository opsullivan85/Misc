#include "ParkedCar.h"
#include "PoliceOfficer.h"
#ifndef PARKINGTICKET_H
#define PARKINGTICKET_H


class ParkingTicket
{
    private:
        int fine;
        ParkedCar car;
        PoliceOfficer officer;
    public:
        ParkingTicket();
        ~ParkingTicket();
        void setParkedCar(ParkedCar);
        void setPoliceOfficer(PoliceOfficer);
        void setHoursIllegalyParked(int);
        int getFine() const {
            return fine
        }

};

#endif // PARKINGTICKET_H
