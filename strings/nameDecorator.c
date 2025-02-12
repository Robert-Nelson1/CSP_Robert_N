// Robert Nelson, Name Decorator - C

#include <stdio.h>
#include <string.h>
char name[20];
int main(void){

    printf("Welcome, what is your name: \n");
    scanf("%s", name);
    char smiley[] = "(: (: (: ";
    char moreSmiley[] = " :) :) :)";
    strcat(smiley, name);
    strcat(smiley, moreSmiley); // can only concatanate one thing at a time
    printf("Hello %s, welcome to my program!", smiley);

    return 0;
}

