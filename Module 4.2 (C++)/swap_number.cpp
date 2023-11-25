/*
Write a program to swap the two numbers using friend function without
using third variable.

*/

#include <iostream>
using namespace std;

class Number
{
private:
    int value;

public:
    Number(int val)
    {
        value = val;
    }

    friend void swapNumbers(Number &num1, Number &num2);
    void display()
    {
        cout << "Value: " << value << endl;
    }
};

void swapNumbers(Number &num1, Number &num2)
{
    num1.value = num1.value + num2.value;
    num2.value = num1.value - num2.value;
    num1.value = num1.value - num2.value;
}

int main()
{
    Number num1(10);
    Number num2(20);

    cout << "Before swapping:" << endl;
    num1.display();
    num2.display();

    swapNumbers(num1, num2);

    cout << "After swapping:" << endl;
    num1.display();
    num2.display();

    return 0;
}
