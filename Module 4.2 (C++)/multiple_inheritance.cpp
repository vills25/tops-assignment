/*Create a class person having members name and age. Derive a class student
having member percentage. Derive another class teacher having member
salary. Write necessary member function to initialize, read and write data.
Write also Main function (Multiple Inheritance) */

#include <iostream>
#include <string>

using namespace std;

class Person
{
protected:
    string name;
    int age;

public:
    void initialize() 
    {
        cout << "Enter name: ";
        cin.ignore();
        getline(cin, name);
        cout << "Enter age: ";
        cin >> age;
        cin.ignore(); // to clear the input buffer
    }

    void display()
    {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class Student : public Person
{
private:
    float percentage;

public:
    void readData()
    {
        initialize();
        cout << "Enter percentage: ";
        cin >> percentage;
    }

    void displayData()
    {
        display();
        cout << "Percentage: " << percentage << "%" << endl;
    }
};

class Teacher : public Person
{
private:
    float salary;

public:
    void readData()
    {
        initialize();
        cout << "Enter salary: ";
        cin >> salary;
    }

    void displayData()
    {
        display();
        cout << "Salary: $" << salary << endl;
    }
};

int main()
{
    Student student;
    Teacher teacher;

    cout << "Enter student details: " << endl;
    student.readData();

    cout << "\nEnter teacher details: " << endl;
    teacher.readData();

    cout << "\nStudent details: " << endl;
    student.displayData();

    cout << "\nTeacher details: " << endl;
    teacher.displayData();

    return 0;
}
