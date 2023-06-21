#include<stdio.h>
#include<conio.h>
int main()
{
    int arr[10], evenCount=0, oddCount=0,i, odd_sum, evem_sum,sum;

    printf("Enter any 10 elements: ");

    for(i=0; i<10; i++)
        scanf("%d", &arr[i]);
    for(i=0; i<10; i++)
    {
        if(arr[i]%2==0)
            evenCount++;
        else
            oddCount++;

        sum = oddCount + evenCount , &odd_sum,&evem_sum;    
    }
    printf("\nTotal Even numbers = %d", evenCount);
    printf("\nTotal Odd numbers = %d", oddCount);
    printf("\nThe Sum of EVEN numbers and Odd numbers is: %d",sum);
    getch();

    return 0;


}    
