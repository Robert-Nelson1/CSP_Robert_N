#include <stdio.h>

int main(void){

char name[20];
int age;
float pi = 3.14;

    printf("Welcome, what is your name: \n");
    scanf("%s", name);
    printf("How old are you: \n");
    scanf("%d", age);
    printf("Tell me how much pi you know")
    scanf("%f", &pi);
    printf("Hello I am %s. I am %d years old. I like the number %f \n", name, age, pi);
    printf("%d\n", age);
    printf("%f\n", pi);
    return 0;
}

