//Robert Nelson, My Family Loop - C
#include <stdio.h>

int main(void){

    char siblings[][20] = {"Robert", "Renee", "John"};
    int mlength = sizeof(siblings)/sizeof(siblings[0]);

    int m;
    for(m=0;m<mlength;m++){
        printf("Hello %s\n", siblings[m]);
    }
    return 0;
}

