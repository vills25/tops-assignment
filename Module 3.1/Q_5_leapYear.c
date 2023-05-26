// Q.5 WAP to check if the given year is a leap year or not.

#include <stdio.h>
int main()

{
    
int y;

printf("Enter any year:  ");
scanf("%d", &y);

if(y%400==0 || y%4==0 && y%100!=0)
{
    printf("Year is Leapyear");
}

else
{
    printf("Year is not leapyear");
}

return 0;
}