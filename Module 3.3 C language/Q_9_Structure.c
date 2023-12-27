#include <stdio.h>
struct employee
{
    int employeeno;
    char name[50];
    int age;
    char address[50];
};

int main()
{
    int a;
    struct employee e;

    printf("Enter Employee no: ");
    scanf("%d", &e.employeeno);

    printf("Enter age: ");
    scanf("%d", &e.age);

    printf("Enter your Address: ");
    scanf(" ");
    gets(e.address);

    printf("Enter your Name: ");
    scanf(" ");
    gets(e.name);

    return 0;

}