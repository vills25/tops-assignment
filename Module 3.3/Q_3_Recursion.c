// Q.3 ---> WAP to find reverse of string using recursion.


// C program to reverse a string using recursion
# include <stdio.h>

/* Function to print reverse of the passed string */
void reverse(char *str)
{
if (*str)
{
	reverse(str+1);
	printf("%c", *str);
}
}

/* Driver program to test above function */
int main()
{
char a[] = "Geeks for Geeks";
reverse(a);
return 0;
}
