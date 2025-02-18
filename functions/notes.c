// Robert Nelson, function notes in C
#include <stdio.h>
int num;
char name[50], place[50], verb[50];
int add(int numOne, int numTwo){
    return numOne+numTwo;
}
const char* word(type){
    char choice[50];
    printf("Please give me a %s:\n", type);
    scanf("%s", choice);
    return choice;
}

int main(void){

    printf("Please tell me a number:\n");
    scanf("%d", num);
    /*
    add(num,10);
    add(4,15);
    add(4,20);
    */
    return 0;
}

