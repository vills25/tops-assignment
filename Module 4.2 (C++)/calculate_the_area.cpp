/*
 Write a program to calculate the area of circle, rectangle and triangle using
Function Overloading
 Rectangle: Area * breadth
 Triangle: ½ *Area* breadth
 Circle: Pi * Area *Area

*/

#include <iostream>
#include <cmath>

using namespace std;

const double PI = 3.14159;

// Function to calculate the area of a rectangle
double calculateArea(double length, double breadth)
{
    return length * breadth;
}

// Function to calculate the area of a triangle
double calculateArea(double base, double height)
{
    return 0.5 * base * height;
}

// Function to calculate the area of a circle
double calculateArea(double radius)
{
    return PI * pow(radius, 2);
}

int main()
{
    double length, breadth, base, height, radius;

    cout << "Enter the length and breadth of the rectangle: ";
    cin >> length >> breadth;
    cout << "Area of the rectangle: " << calculateArea(length, breadth) << endl;

    cout << "Enter the base and height of the triangle: ";
    cin >> base >> height;
    cout << "Area of the triangle: " << calculateArea(base, height) << endl;

    cout << "Enter the radius of the circle: ";
    cin >> radius;
    cout << "Area of the circle: " << calculateArea(radius) << endl;

    return 0;
}
