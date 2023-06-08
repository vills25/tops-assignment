//  Q_3------- WAP to find number is even or odd using ternary operator.


#include <stdio.h>
int main()
{
  int num;

    printf("Enter Number: ");
    scanf("%d", &num);

    //  if (num % 2 == 0)
    // {
    //     printf("EVEN");
    // }
    // else 
    // {
    //     printf("ODD");
    // }

   // ----> Using ternary operator... 

num % 2 == 0 ?printf("EVEN"):printf("ODD");
    return 0;




} 