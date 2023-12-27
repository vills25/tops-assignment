/*
    Q.2  WAP to swap two numbers without using third variable
 
*/


#include <stdio.h>
int main()

{

int a, b,num;

printf("Enter number : ");
scanf("%d",&num);
for(int i=0;i < num;i++)
{
    printf("\nEnter first number : ");
    scanf("%d",&a);
    printf("Enter second number : ");
    scanf("%d",&b);

    
    printf("\nBefore swap a=%d b=%d",a,b);      
    a=a+b;//a=30 (10+20)    
    b=a-b;//b=10 (30-20)    
    a=a-b;//a=20 (30-10)    
    printf("\nAfter swap a=%d b=%d",a,b); 
}

   
return 0;  

}