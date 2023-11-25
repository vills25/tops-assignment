/*
Write a program of Addition, Subtraction, Division, Multiplication using
constructor.

*/

#include <iostream>
using namespace std;

class Calculator
{
private:
    double operand1;
    double operand2;

public:
    Calculator(double op1, double op2)
    {
        operand1 = op1;
        operand2 = op2;
    }

    double add()
    {
        return operand1 + operand2;
    }

    double subtract()
    {
        return operand1 - operand2;
    }

    double divide()
    {
        if (operand2 != 0)
        {
            return operand1 / operand2;
        }
        else
        {
            cout << "Error: Division by zero is not allowed." << endl;
            return 0.0;
        }
    }

    double multiply()
    {
        return operand1 * operand2;
    }
};

int main()
{
    double num1, num2;

    cout << "Enter operand 1: ";
    cin >> num1;

    cout << "Enter operand 2: ";
    cin >> num2;

    Calculator calc(num1, num2);

    cout << "Addition: " << calc.add() << endl;
    cout << "Subtraction: " << calc.subtract() << endl;
    cout << "Division: " << calc.divide() << endl;
    cout << "Multiplication: " << calc.multiply() << endl;

    return 0;
}
