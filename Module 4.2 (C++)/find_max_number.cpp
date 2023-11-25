/*
Write a program to find the max number from given two numbers using
friend function.

*/

#include <iostream>
using namespace std;

class MaxFinder
{
private:
    int num1;
    int num2;

public:
    MaxFinder(int a, int b)
    {
        num1 = a;
        num2 = b;
    }

    friend int findMax(const MaxFinder &obj);
};

int findMax(const MaxFinder &obj)
{
    return (obj.num1 > obj.num2) ? obj.num1 : obj.num2;
}

int main()
{
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    MaxFinder mf(num1, num2);
    int maxNumber = findMax(mf);

    cout << "The maximum number is: " << maxNumber << endl;

    return 0;
}
