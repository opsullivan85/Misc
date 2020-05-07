//Ch 11 Project: Weather Stats
//Owen Sullivan 5/25/18
//This program prompts the user for weather data from each month
//And then displays various data for the entire year

//{ Includes
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

//This is the WeatherData structure
struct WeatherData{
    double totalRainfall;
    double highTemp;
    double lowTemp;
    double avgTemp;
};

//{ Function Prototypes
WeatherData* getMonthsData();
void displayYearData(WeatherData*);
  double getAverageMonthlyRainfall(WeatherData*);
  double getTotalRainfall(WeatherData*);
  int getHighTempMonth(WeatherData*);
  int getLowTempMonth(WeatherData*);
  double getAverageTemp(WeatherData*);
//}

//This is an enum consisting of all the months
enum MonthEnum{ JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC};

//This is the constant string array consisting of all the months
const string monthStrings[] = {"January",
                         "February",
                         "March",
                         "April",
                         "May",
                         "June",
                         "July",
                         "August",
                         "September",
                         "October",
                         "November",
                         "December"};

int main(){
    //Sets the text formatting and displays the program name
    cout << setprecision(1) << left << fixed << "Ch 11 Project: Weather Stats\n\n";

    //Initializes an array to hold the weather data for each month
    WeatherData *data = new WeatherData[12];

    //Populates the array with user inputed data
    data = getMonthsData();

    //Calculates and displays data for the entire year using the monthly data
    displayYearData(data);
}

//This function prompts the user for each month's data
//The data for each month is put into an array of WeatherData structures
//The function then returns a pointer to this array
WeatherData* getMonthsData(){
    //Initializes the WeatherData array
    WeatherData *data = new WeatherData[12];

    //Prompts for each month's data, does bounds checking where applicable
    //and then puts the data into the structures of the array
    for(int month = JAN; month <= DEC; month++){
        cout << monthStrings[month] << "'s Weather Data:\n";

        cout << "  *Total Rainfall?: ";
        cin >> data[month].totalRainfall;

        do{
        cout << "  *High Temperature?: ";
        cin >> data[month].highTemp;
        } while(data[month].highTemp < -100 || data[month].highTemp > 140);

        do{
        cout << "  *Low Temperature?: ";
        cin >> data[month].lowTemp;
        } while(data[month].lowTemp < -100 || data[month].lowTemp > 140);

        do{
        cout << "  *Average Temperature?: ";
        cin >> data[month].avgTemp;
        } while(data[month].avgTemp < -100 || data[month].avgTemp > 140);

        cout << endl;
    }

    return data;
}

//This function accepts a pointer to a WeatherData array
//then displays various data about the year
void displayYearData(WeatherData *data){
    //Initializes variables for high temp, low temp and the months they were in
    int highTempMonthIndex = getHighTempMonth(data);
    int lowTempMonthIndex = getLowTempMonth(data);
    double highTemp = data[highTempMonthIndex].highTemp;
    double lowTemp = data[lowTempMonthIndex].lowTemp;
    string highTempMonth = monthStrings[highTempMonthIndex];
    string lowTempMonth = monthStrings[lowTempMonthIndex];

    //Displays the year's weather data
    cout << "The Year's Weather Data:/n";
    cout << "  *Average Monthly Rainfall: " << getAverageMonthlyRainfall(data) << endl;
    cout << "  *Total Rainfall: " << getTotalRainfall(data) << endl;
    cout << "  *Highest Temperature:\n";
    cout << "    *" << highTemp << " degrees" << endl;
    cout << "    *During: " << highTempMonth << endl;
    cout << "  *Lowest Temperature:\n";
    cout << "    *" << lowTemp << " degrees" << endl;
    cout << "    *During: " << lowTempMonth << endl;
    cout << "  *Average Temperature: " << getAverageTemp(data) << " degrees\n";
}

//This function accepts a pointer to a WeatherData array
//It returns the average monthly rainfall as a double
double getAverageMonthlyRainfall(WeatherData *data){
    int total = 0;

    for(int month = JAN; month <= DEC; month++)
        total += data[month].totalRainfall;

    return(total / 12);
}

//This function accepts a pointer to a WeatherData array
//It returns the total rainfall as a double
double getTotalRainfall(WeatherData *data){
    int total = 0;

    for(int month = JAN; month <= DEC; month++)
        total += data[month].totalRainfall;

    return total;
}

//This function accepts a pointer to a WeatherData array
//It returns the index of the month in the array with the highest temperature
//The index can be used to find the hottest month and its high temperature
int getHighTempMonth(WeatherData *data){
    int highMonth = 0;

    for(int month = JAN; month <= DEC; month++)
        if(data[highMonth].highTemp < data[month].highTemp)
            highMonth = month;

    return highMonth;
}

//This function accepts a pointer to a WeatherData array
//It returns the index of the month in the array with the lowest temperature
//The index can be used to find the coldest month and its low temperature
int getLowTempMonth(WeatherData *data){
    int lowMonth = 0;
    for(int month = JAN; month <= DEC; month++)
        if(data[lowMonth].lowTemp > data[month].lowTemp)
            lowMonth = month;

    return lowMonth;
}

//This function accepts a pointer to a WeatherData array
//It returns the average temperature as a double
double getAverageTemp(WeatherData *data){
    int total = 0;

    for(int month = JAN; month <= DEC; month++)
        total += data[month].avgTemp;

    return(total / 12);
}
