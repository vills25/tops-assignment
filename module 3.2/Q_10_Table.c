// Q.10  Write a programe to print table up to given numbers.

#include <stdio.h>
int main()
{
    int num;
    printf("Enter Number: ");
    scanf("%d", &num);
    int i = 1;
    while (i <= 10)
    {
        printf("%d x %d =%d\n", num, i, i * num);
        i++;
    }

    return 0;
}