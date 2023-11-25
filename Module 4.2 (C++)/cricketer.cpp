/*
Assume a class cricketer is declared. Declare a derived class batsman from
cricketer. Data member of batsman. Total runs, Average runs and best
performance. Member functions input data, calculate average runs, Display
data. (Single Inheritance)
*/

#include <iostream>
using namespace std;

class Cricketer
{
protected:
    string name;

public:
    void inputData()
    {
        cout << "Enter the name of the cricketer: ";
        cin >> name;
    }
};

class Batsman : public Cricketer
{
private:
    int runs[5];

public:
    void inputData()
    {
        Cricketer::inputData();
        cout << "Enter the runs scored in 5 matches: ";
        for (int i = 0; i < 5; i++)
        {
            cin >> runs[i];
        }
    }

    int calculateTotalRuns()
    {
        int total = 0;
        for (int i = 0; i < 5; i++)
        {
            total += runs[i];
        }
        return total;
    }

    float calculateAverageRuns()
    {
        int total = calculateTotalRuns();
        return static_cast<float>(total) / 5.0;
    }

    int findBestPerformance()
    {
        int best = runs[0];
        for (int i = 1; i < 5; i++)
        {
            if (runs[i] > best)
            {
                best = runs[i];
            }
        }
        return best;
    }

    void displayData()
    {
        cout << "\nBatsman Name: " << name << endl;
        cout << "Total Runs: " << calculateTotalRuns() << endl;
        cout << "Average Runs: " << calculateAverageRuns() << endl;
        cout << "Best Performance: " << findBestPerformance() << endl;
    }
};

int main()
{
    Batsman batsman;
    batsman.inputData();
    batsman.displayData();
    return 0;
}
