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



int main(void){

    printf("Hello World");

    // print statement that welcomes my user and tells what the program does
printf("\nHi, this is a financial calculator, it will ask you questions to help you make good financial decisions");
//ask user their income (variable and input)
printf("\nwhat is your monthly income?");
scanf("%f", &income);

//ask user their rent (variable and input)
printf("\nwhat is your rent?");
scanf("%f", &rent);

// ask user their utilities (variable and input)
printf("\nwhat is your utilities?");
scanf("%f", &utilities);

// ask user their groceries (variable and input)
printf("\nwhat is your groceries?");
scanf("%f", &groceries);

// ask user their transportation (variable and input)
printf("\nwhat is your transportation?");
scanf("%f", &transportation);

// calculate percent income of rent (rent/income*100) variable
percentRent = rent/income*100;
//calculate percent income of utilities (utilities/income*100) variable
percentUtilities = utilities/income*100;
// calculate percent income of groceries (groceries/income*100) variable
percentGroceries = groceries/income*100;
// calculate percent income of transportation (transportation/income*100) variable
percentTransportation = transportation/income*100;

// calculate savings as 10% income (income*.1) (variable)
savings = (income*.1);
// calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = (income-savings-rent-utilities-groceries-transportation);


// Your rent is $XX.XX which is XX% of your income. (Print)
printf("\nYour rent is $%.2f, which is %.1f percent of your income", rent, percentRent);
// Your utilities is $XX.XX which is XX% of your income. (Print)
printf("\nYour utilities is $%.2f, which is %.1f percent of your income", utilities, percentUtilities);
// Your groceries is $XX.XX which is XX% of your income. (Print)
printf("\nYour groceries is $%.2f, which is %.1f percent of your income", groceries, percentGroceries);
// Your transportation is $XX.XX which is XX% of your income. (Print)
printf("\nYour transportation is $%.2f, which is %.1f percent of your income", transportation, percentTransportation);
// Your savings is $XX.XX which is XX% of your income. (Print)
printf("\nYou should save 10%% of your income, which is $%.2f", savings);
// Your spending is $XX.XX which is XX% of your income. (Print)
printf("\nYou should only spend $%.2f, otherwise you will go in debt", spending);
    return 0;
}

