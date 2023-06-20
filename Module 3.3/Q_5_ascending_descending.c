// Q.5 ---> WAP to take two Array input from user and sort them in ascending or descending order as per user’s choice.


#include <stdio.h>       //including stdio.h for printf and other functions
#include<conio.h>


int main()     //default function for call
{
	int a[100],n,i,j;
	printf("Array size: ");
        scanf("%d",&n);
        printf("Elements: ");
        
      for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
	for (int i = 0; i < n; i++)            //Loop for ascending ordering
	{
		for (int j = 0; j < n; j++)        //Loop for comparing other values
		{
			if (a[j] > a[i])               //Comparing other array elements
			{
				int tmp = a[i];           //Using temporary variable for storing last value
				a[i] = a[j];              //replacing value
				a[j] = tmp;              //storing last value
			}   
		}
	}
	printf("\n\nAscending : ");          //Printing message
	for (int i = 0; i < n; i++)          //Loop for printing array data after sorting
	{
		printf(" %d ", a[i]);
	}
	for (int i = 0; i < n; i++)          //Loop for descending ordering
	{
		for (int j = 0; j < n; j++)             //Loop for comparing other values
		{
			if (a[j] < a[i])                //Comparing other array elements
			{
				int tmp = a[i];         //Using temporary variable for storing last value
				a[i] = a[j];            //replacing value
				a[j] = tmp;             //storing last value
			}
		}
	}
	printf("\n\nDescending : ");            //Printing message
	for (int i = 0; i < n; i++)             //Loop for printing array data after sorting
	{
		printf(" %d ", a[i]);               //Printing data
	}

	return 0;          //returning 0 status to system
getch();
}

//Ouput
/*

Array size: 10

Elements :  3  4  7  6  5  1  2  8  10  9

Ascending :  1  2  3  4  5  6  7  8  9  10

Descending :  10  9  8  7  6  5  4  3  2  1
*/
