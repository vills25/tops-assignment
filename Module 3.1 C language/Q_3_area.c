// Q.3  WAP to find area of circle, rectangle and triangle


// multi function c programme to find the area of a triangle, rectangle and circle
#include <stdio.h>
// function to compute the area of a triangle, it will return a floating value
float tri(float b, float h)
{
    float Area = 0.5*b*h;
    return Area;
}
// function to compute the area of a rectangle
float rec(float l, float w)
{
   float Area = l*w;
   return Area;
}

// function to compute the area of a circle
float cir(float r)
{
    float Area = (22.0/7)*(r*r);
    //(22.0/7.0) is pi
    return Area; 
}
// the main function
int main()
{
    printf("PROGRAMME TO COMPUTE THE AREA OF A TRIANGLE, RECTANGLE OR CIRCLE");
    printf("\n\nMENU\nEnter 1 for a triangle\n2 for a rectangle\n3 for a circle\n");
    int command;
    scanf("%d", &command);
    if(command==1)
    {
        printf("\nEnter\nbase:  ");
        float base, height, Area;
        scanf("%f", &base);
        printf("height:  ");
        scanf("%f", &height);
        Area = tri(base, height);
        printf("\nArea = %.2f", Area);

    }
    else if (command==2)
    {
       printf("\nEnter\nlength:  ");
       float l, w, Area;
       scanf("%f", &l);
       printf("width:  ");
       scanf("%f", &w);
       Area = rec(l,w);
       printf("\nArea = %.2f", Area);
       
    }

    else if (command==3)
    {
        printf("\nEnter radius:  ");
        float r, Area;
        scanf("%f", &r);
        Area = cir(r);
        printf("\nArea = %.2f",Area);
    }

    else
    {
        printf("Run again for a right menu!!!");
    }
    return 0;
     
}