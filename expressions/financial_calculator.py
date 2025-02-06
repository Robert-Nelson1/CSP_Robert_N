# Robert Nelson, Financial Calculator - Python

# print statement that welcomes my user and tells what the program does
print("Hi, this is a financial calculator, it will ask you questions to help you")
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
print("Your savings is", savings, "% of your income")
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = income-savings-rent-utilities-groceries-transportation
print(spending)
# calculate percent income of rent (rent/income*100) variable
percent_of_rent = rent/income*100
print("Your percent of rent is", percent_of_rent)

# calculate percent income of utilities (utilities/income*100) variable
percent_of_utilities = utilities/income*100
# calculate percent income of groceries (groceries/income*100) variable
percent_of_groceries = groceries/income*100
# calculate percent income of transportation (transportation/income*100) variable
percent_of_transportation = transportation/income*100
# calculate percent income of spending (spending/income*100) variable

# Your rent is $XX.XX which is XX% of your income. (Print)

# Your utilities is $XX.XX which is XX% of your income. (Print)

# Your groceries is $XX.XX which is XX% of your income. (Print)

# Your transportation is $XX.XX which is XX% of your income. (Print)

# Your savings is $XX.XX which is XX% of your income. (Print)

# Your spending is $XX.XX which is XX% of your income. (Print)
