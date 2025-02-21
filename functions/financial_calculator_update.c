// Robert Nelson, Update your Financial Calculator - C
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

void money(float *var, const char *categorytype){
    printf("What is your %s: ", categorytype);
    scanf("%f", var);
}

void financial(float cost, float income, const char *type[20]){
    
    float percent = cost/income*100;
    
    printf("\nYour %s is $%.2f, which is %.2f%% of your income.", type, cost, income);
    
}



int main(void){


    // print statement that welcomes my user and tells what the program does
printf("\nHi, this is a financial calculator, it will ask you questions to help you make good financial decisions\n");
// This is asking the user what their ______ is.
money(&income, "income");
money(&rent, "rent");
money(&utilities, "utilities");
money(&groceries, "groceries");
money(&transportation, "transportation");

// calculate savings as 10% income (income*.1) (variable)
savings = income*.1;
// calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = income-savings-rent-utilities-groceries-transportation;


// This is telling the user what their ______ is and what percent of their income it is.
financial(rent, income, "rent");
financial(utilities, income, "utilities");
financial(groceries, income, "groceries");
financial(transportation, income, "transportation");

financial(savings, income, "savings");
financial(spending, income, "spending");

}

