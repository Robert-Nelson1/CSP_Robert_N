//Robert Nelson, Old Enough - C
#include <stdio.h>
#include <string.h> //needed to compare strings
char name[20];
int num;
int main(void){
    
    printf("Hello, what is your name?\n");
    scanf("%s", name);
    printf("Hello %s, \n", name);
    
    printf("How old are you?\n");
    scanf("%d", &num);
    if(num == 0){
        printf("How can you type at 0?\n");
    }else if(num >= 18){
        printf("You can vote.\n");
    }else if(num >= 16){
        printf("You can drive.\n");
    }else if(num >= 15){
        printf("You can get a learners permit.\n");
    }else if(num >= 5){
        printf("You can go to school.\n");
    }else{
        printf("You can't vote, drive, get a learners permit, and go to school.\n");
    }

    return 0;
}

