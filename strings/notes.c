// Robert Nelson, Strings Notes C
#include <stdio.h>
#include <string.h>
int main(void){
char subject[50];
char name[] = "Victoria";
char sentence[] = "The quick brown fox jumps over the lazy dog";


    /*
    printf("What class are you in?\n");
    scanf("%s", subject);
    fgets(subject, 50, stdin);
    printf("You are in %s, that is a cool class", subject);
    */
    name[0] = 'T';
    name[1] = 'o';
    name[2] = 'r';
    name[3] = 'i';
    //int size = (sizeof(sentence));
   // printf("%s\n", name);
    printf("%lu\n", sizeof(sentence)); // goes by index, starts at 0
    printf("%d", strlen(sentence)); // count the number of chachater, starts at 0
    char one[] = "Hello ";
    char two[] = "World!";
    char three[] = "Welcome to my program. ";
    printf("%s", one);
    strcat(one, two);
    printf("%s", one);
    strcat(three, one); // can only concatanate one thing at a time
    printf("%s", three);
    return 0;
}

