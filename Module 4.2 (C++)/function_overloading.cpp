/* 
    Write a program to Mathematic operation like Addition, Subtraction,
  Multiplication, Division Of two number using different parameters and
  Function Overloading  */

#include <iostream>

// Function to add two numbers
int mathOperation(int a, int b)
{
    return a + b;
}

// Function to subtract two numbers
int mathOperation(int a, int b, int c)
{
    return a - b - c;
}

// Function to multiply two numbers
float mathOperation(float a, float b)
{
    return a * b;
}

// Function to divide two numbers
float mathOperation(float a, int b)
{
    return a / b;
}

int main()
{
    int x = 10, y = 5;
    float f1 = 12.5, f2 = 2.5;

    // Addition
    int sum = mathOperation(x, y);
    std::cout << "Sum: " << sum << std::endl;

    // Subtraction
    int difference = mathOperation(x, y, 3);
    std::cout << "Difference: " << difference << std::endl;

    // Multiplication
    float product = mathOperation(f1, f2);
    std::cout << "Product: " << product << std::endl;

    // Division
    float quotient = mathOperation(f1, y);
    std::cout << "Quotient: " << quotient << std::endl;

    return 0;
}
