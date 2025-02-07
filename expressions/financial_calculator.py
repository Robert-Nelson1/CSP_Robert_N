# Robert Nelson, Financial Calculator - Python

# print statement that welcomes my user and tells what the program does
print("Hi, this is a financial calculator, it will ask you questions to help you make good finicial decisions")
# ask user their income (variable and input)
income = float(input("What is your income?\n"))
# ask user their rent (variable and input)
rent = float(input("What is your rent?\n"))

# ask user their utilities (variable and input)
utilities = float(input("What is your utilities?\n"))

# ask user their groceries (variable and input)
groceries = float(input("What is your groceries?\n"))

# ask user their transportation (variable and input)
transportation = float(input("What is your transportation?\n"))

# calculate savings as 10% income (income*.1) (variable)
savings = income*.1
print("You should be saving 10% of your income which is $", savings)
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = income-savings-rent-utilities-groceries-transportation
print("You should spend only $", spending, "otherwise you will go in debt")
# calculate percent income of rent (rent/income*100) variable
percent_of_rent = rent/income*100
print("Your percent of rent is", percent_of_rent, "%")

# calculate percent income of utilities (utilities/income*100) variable
percent_of_utilities = utilities/income*100
print("Your percent of utilities is", percent_of_utilities, "%")
# calculate percent income of groceries (groceries/income*100) variable
percent_of_groceries = groceries/income*100
print("Your percent of groceries is", percent_of_groceries, "%")
# calculate percent income of transportation (transportation/income*100) variable
percent_of_transportation = transportation/income*100
print("Your percent of transportation is", percent_of_transportation, "%")

# calculate percent income of spending (spending/income*100) variable
percent_of_spending = spending/income*100
print("Your percent of spending is", percent_of_spending, "%")
# Your rent is $XX.XX which is XX% of your income. (Print)
print("Your rent is $", rent, "which is ", percent_of_rent, "%", "of your income" )
# Your utilities is $XX.XX which is XX% of your income. (Print)
print("Your utilities is $", utilities, "which is ", percent_of_utilities, "%", "of your income" )
# Your groceries is $XX.XX which is XX% of your income. (Print)
print("Your groceries is $", groceries, "which is ", percent_of_groceries, "%", "of your income" )
# Your transportation is $XX.XX which is XX% of your income. (Print)
print("Your transportation is $", transportation, "which is ", percent_of_transportation, "%", "of your income" )

# Your savings is $XX.XX which is XX% of your income. (Print)
print("Your savings is $", savings, "which is 10% of your income" )

# Your spending is $XX.XX which is XX% of your income. (Print)
print("Your spending is $", spending, "which is ", percent_of_spending, "%", "of your income" )