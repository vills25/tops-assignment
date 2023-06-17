// Q.9 06 Diffrents Paterns with C languague.

//-----> patern type (1)

//  1
//  1 0
//  1 0 1
//  1 0 1 0
//  1 0 1 0 1

// C program to print right half pyramid pattern of number
    // #include<stdio.h>
    // int main()
    // {
    //    int i,j,n;
    //    printf("Enter how many rows you want : ");
    //    scanf("%d",&n);
    //    for(i=1; i<=n; i++)
    //    {
    
    //     for(j=1; j<=i; j++)
    //         printf(" %d", j%2);
        
    //     printf("\n");
    //    }
    //    return 0;
    // }

// -------------------------------------------------------------------------------------------------------------------



/*  --------> Patern type (2) 

         * 
       * * *
     * * * * *
   * * * * * * * 
 * * * * * * * * *
 
 */

// C program to print the full pyramid pattern of stars


    //   #include <stdio.h>
      
    //   int main()
    //   {
    //       int rows = 5;
      
    //       // first loop to print all rows
    //       for (int i = 0; i < rows; i++) 
    //       {
      
    //           // inner loop 1 to print white spaces
    //           for (int j = 0; j < 2 * (rows - i) - 1; j++) 

    //           {
    //               printf(" ");
    //           }
      
    //           // inner loop 2 to print star * character
    //           for (int k = 0; k < 2 * i + 1; k++) 

    //           {
    //               printf("* ");
    //           }
    //           printf("\n");
    //       }
    //       return 0;
    //   }


//  --------------------------------------------------------------------------------------------------------


// -------->  Patern type (3)
/*
     A 
     B C
     D E F 
     G H I J 
     K L M N O

*/

      // #include <stdio.h>
      // int main()
      // {
      // 	int i, j;
      // 	int rows = 5;


      // 	char character = 'A';


      // 	for (i = 0; i < rows; i++)
      // 	{
          
      // 		for (j = 0; j <= i; j++)
      // 		{
      // 		  printf("%c ",character);
      // 			character++;
      // 		}
      // 		printf("\n");
      // 	}

      // 	return 0;

      // }

//-----------------------------------------------------------------------------------------------

// -------> Patern type (4)

//  *
//  * *
//  * * *
//  * * * *
//  * * * * *
//  * * * *
//  * * * 
//  * * 
//  *

    // #include<stdio.h>
    // int main()
    // {
    //     int i,j,k,n;
    //     printf("Enter the value for n: ");
    //     scanf("%d",&n);
    
    //     for(i=-n;i<=n;i++) // Note that ‘i’ is starting from -n (negative n)
    //     {
    //         k=i;
    //         if(k<0)
    //             k= k*-1;
    
    //         for(j=0;j<=n;j++)
    //         {
    //             if(k<=j)
    //                 printf("* ");
    //         }
    //         printf("\n");
    //     }
    //         return 0;
    // }

// -------------------------------------------------------------------------------------------------------

//  -------> Patern Type (5)

    // #include<stdio.h>
    // int main()
    // {
    //     int i,j,n;
        
    //     // 'count' variable to count the numbers
    //     int count=0;
        
    //     // Take input from the user. Num of rows to print
    //     printf("Enter how many rows you want : ");
    //     scanf("%d",&n);
        
    //     // Loop until we reach row value
    //     for(i=1;i<=n;i++)
    //     {
    //         for(j=1;j<=i;j++)
    //         {
    //             // At each number, Increase the value of 'count' and display
    //             count++;
    //             printf(" %d",count);
    //         }
            
    //         printf("\n");
    //     }
    //     return 0;
    // }

// --------------------------------------------------------------------------------------------------------------

// ------> Patern type (6)

    // #include <stdio.h>
    // int main()
    // {
    //     int i, j;
    //     for(i=1;i<=6;i++)
    //     {
    //         for(j=1;j<=i;j++)
    //         {
    //             printf("%c",'A' + j-1);
    //         }
    //         printf("\n");
    //     }
    //     return 0;
    // }



