//Robert Nelson, Conditional notes C
#include <stdio.h>
#include <string.h> //needed to compare strings
char name[]= "Robert";
int num;
int main(void){


    // 10. How do you write an if statement in C?
    if(strcmp(name, "Robert") == 0){ //strcmp means string comparison when the outcome is 0 the strings are the same
        printf("Hello Nelson, welcome to class\n");
    // 11. How do you write else statements in C?
    }else{
        printf("Hello %s, \n", name);
    }
    printf("How many siblings do you have?\n");
    scanf("%d", &num);
    // 12. How do you write elif/ else if statements in C?
    if(num == 0){
        printf("You are an only child\n");
    }else if(num <= 2){
        printf("You have a couple of siblings\n");
    }else if(num <= 5){
        printf("You have a few siblings\n");
    }else if(num <= 5){
        printf("You have a lot of siblings\n");
    }
    // 13. How do you write the 3 logical operators in C?
    // && = and
    // || = or
    // ! = not

    if(num == 7 || num == 13){
        printf("This an unlucky number\n", num);
    }else if (num <10 && num >5){
        printf("%d is a large single digit number\n", num);
    }else if (!num > 10){
        if(num == 12){
            printf("That is a dozen!\n")
        }
        printf("%d is a big number\n", num);
    }else{
        printf("You typed in %d\n", num);
    }


    return 0;
}

