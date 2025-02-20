// Robert Nelson, Update Hello World - C
#include <stdio.h>

void username(char name[9]){
    printf("Your name is %s\n", name);
}

int main(void){
  
    username("John");
    username("James");
    username("Henry");
    username("Jerry");
    username("Tom");
    
    return 0;
}

