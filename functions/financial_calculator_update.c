// Robert Nelson, Financial Calculator - C
#include <stdio.h>
float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spending;
float percentRent;
float percentUtilities;
float percentGroceries;
float percentTransportation;

//int cost;
//char type;

void money(float var, char categorytype[20]){
    printf("What is your %s: ", categorytype);
    scanf("%f", var);
}

void financial(float cost, float income, char type[20]){
    
    float percent = cost/income*100;
    printf("What is your %f", income);
    
    printf("Your %s is $%f, which is %f%% of your income.", type, cost, income);
    
}



int main(void){


    // print statement that welcomes my user and tells what the program does
printf("\nHi, this is a financial calculator, it will ask you questions to help you make good financial decisions\n");

money(income, "income");
money(rent, "rent");
money(utilities, "utilities");
money(groceries, "groceries");
money(transportation, "transportation");
financial(rent, income, "rent");


}

