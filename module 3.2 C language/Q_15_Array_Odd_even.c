#include <stdio.h>
#include <conio.h>
int main()
{
    int arr[10], evenCount = 0, oddCount = 0, i, odd_sum = 0, evem_sum = 0, sum;

    printf("Enter any 10 elements: ");

    for (i = 0; i < 10; i++)
        scanf("%d", &arr[i]);
    for (i = 0; i < 10; i++)
    {
        if (arr[i] % 2 == 0)
        {
            evenCount++;
            evem_sum = evem_sum + arr[i];
        }
        else
        {
            oddCount++;
            odd_sum = odd_sum + arr[i];
        }

        sum = oddCount + evenCount;
    }
    printf("\nTotal Even numbers = %d", evenCount);
    printf("\nTotal Odd numbers = %d", oddCount);
    printf("\nTotal of even sum = %d",evem_sum );
    printf("\nTotal of odd numbers= %d", odd_sum);
    getch();

    return 0;
}
