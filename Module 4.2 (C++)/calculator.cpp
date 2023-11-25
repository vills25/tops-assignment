#include <iostream>

using namespace std;

class Calculator
{
public:
    int add(int a, int b)
    {
        return a + b;
    }

    int subtract(int a, int b)
    {
        return a - b;
    }

    int multiply(int a, int b)
    {
        return a * b;
    }

    double divide(int a, int b)
    {
        if (b == 0)
        {
            cout << "Error: Cannot divide by zero!" << endl;
            return 0;
        }
        return static_cast<double>(a) / b;
    }
};

int main()
{
    Calculator calculator;

    int a, b;
    char op;

    cout << "Enter the first number: ";
    cin >> a;
    cout << "Enter the operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter the second number: ";
    cin >> b;

    switch (op)
    {
    case '+':
        cout << "Result: " << calculator.add(a, b) << endl;
        break;
    case '-':
        cout << "Result: " << calculator.subtract(a, b) << endl;
        break;
    case '*':
        cout << "Result: " << calculator.multiply(a, b) << endl;
        break;
    case '/':
        cout << "Result: " << calculator.divide(a, b) << endl;
        break;
    default:
        cout << "Invalid operator!" << endl;
        break;
    }

    return 0;
}
