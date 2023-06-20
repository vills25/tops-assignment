#include <stdio.h>
struct employee
{
   int empno;
   int age;
   char address[50];
   char name[50];
};

int main()
{
   int a;
   struct employee e[5];
    for (int i = 0; i < 5; i++)

    {
     printf("Enter your employee ID: ");
     scanf("%d", &e[i].empno);
     
     printf("Enter your age: ");
     scanf("%d", &e[i].age);

     printf("Enter your address: ");
     scanf(" ");
     gets(e[i].address);

     printf("Enter your Name: ");
     scanf(" ");
     gets(e[i].name);

     return 0;

    }

}