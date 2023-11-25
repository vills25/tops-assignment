// Write a program of to swap the two values using templates.

#include <iostream>

// Function template to swap two values
template <typename T>
void swapValues(T &a, T &b)
{
    T temp = a;
    a = b;
    b = temp;
}

int main()
{
    using namespace std;

    // Swap two integers
    int x = 5;
    int y = 10;
    cout << "Before swap: x = " << x << ", y = " << y << endl;
    swapValues(x, y);
    cout << "After swap: x = " << x << ", y = " << y << endl;

    // Swap two floating-point numbers
    double a = 3.14;
    double b = 2.71;
    cout << "Before swap: a = " << a << ", b = " << b << endl;
    swapValues(a, b);
    cout << "After swap: a = " << a << ", b = " << b << endl;

    return 0;
}
