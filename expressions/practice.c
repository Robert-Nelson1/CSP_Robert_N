// Robert Nelson, Expressions Practice - C
#include <stdio.h>
#include <math.h>
int one = 7-24/8*4+6;
int two = 18/3-7+2*5;
int three = 6*4/12+72/8-9;
int four = (17-6/2)+4*3;
int five = -2*(1*4-2/2)+(6+2-3);
int six = -1*((3-4*7)/5)-2*24/6;
int seven = (3*(int)pow(5, 2)/15)-(5-(int)pow(2, 2));
int eight = (int)pow(1, 4)*(int)pow(2, 2)+(int)pow(3, 3)-(int)pow(2, 5)/4;
int nine = (int)pow(22/2-2*5, 2)+(int)pow(4-6/6, 2);

int main(void){
    printf("%d\n", one);
    printf("%d\n", two);
    printf("%d\n", three);
    printf("%d\n", four);
    printf("%d\n", five);
    printf("%d\n", six);
    printf("%d\n", seven);
    printf("%d\n", eight);
    printf("%d\n", nine);
    return 0;
}
