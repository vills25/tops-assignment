/*Assume that the test results of a batch of students are stored in three different
classes. Class Students are storing the roll number. Class Test stores the marks
obtained in two subjects and class result contains the total marks obtained in
the test. The class result can inherit the details of the marks obtained in the
test and roll number of students. (Multilevel Inheritance)  */

#include <iostream>
using namespace std;

// Base class: Students
class Students
{
protected:
    int rollNumber;

public:
    void setRollNumber(int rollNumber)
    {
        this->rollNumber = rollNumber;
    }
    int getRollNumber()
    {
        return rollNumber;
    }
};

// Intermediate class: Test (inherits from Students)
class Test : public Students
{
protected:
    int subject1Marks;
    int subject2Marks;

public:
    void setMarks(int subject1Marks, int subject2Marks)
    {
        this->subject1Marks = subject1Marks;
        this->subject2Marks = subject2Marks;
    }
    void displayMarks()
    {
        cout << "Subject 1 Marks: " << subject1Marks << endl;
        cout << "Subject 2 Marks: " << subject2Marks << endl;
    }
};

// Derived class: Result (inherits from Test)
class Result : public Test
{
private:
    int totalMarks;

public:
    void calculateTotalMarks()
    {
        totalMarks = subject1Marks + subject2Marks;
    }
    void displayResult()
    {
        cout << "Roll Number: " << getRollNumber() << endl;
        displayMarks();
        cout << "Total Marks: " << totalMarks << endl;
    }
};

int main()
{
    Result result;
    result.setRollNumber(1);
    result.setMarks(85, 90);
    result.calculateTotalMarks();
    result.displayResult();

    return 0;
}
