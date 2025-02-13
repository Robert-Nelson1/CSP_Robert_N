// Robert Nelson, silly sentences C
#include <stdio.h>
// empty string variables for user words (minimum 3)

char name[20];
char adjective[20];
char noun[20];

int main(void){


    // A welcome for the user telling them what the program is (print)
    printf("Welcome, this program is going to make a silly sentence and is going to ask you easy questions. \nWhat is your name: \n");
    scanf("%s", name);

    //ask user for words (print statement with a question scanf to set to) (in C we need to tell the user we can only write one word.)
    printf("Give me an verb!:\n");
    scanf("%s", adjective);

    printf("Give me an noun!:\n");
    scanf("%s", noun);

    //print out story with the variables inserted ("welcome %s to my program", name)
    printf("You, %s will %s to your %s \n", name, adjective, noun);


    return 0;
}

