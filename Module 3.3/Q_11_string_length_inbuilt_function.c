// Q_11_ WAP Find out length of string without using inbuilt function.


#include <stdio.h>

int main()
{
    int length = 0;
    char string[30];

    // input the string
    printf("Enter the string: \n");
    gets(string);

    // Traversing until a backspace character is encountered which mark end of string
    while (string[length] != '\0')
        length++;
    printf("Length of string is: %d", length);

    return 0;
}