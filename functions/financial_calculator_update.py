# Robert Nelson, Update your Financial Calculator - Python

def info(cost, income, category):
    percent = cost/income*100
    print(f"Your {category} is ${cost:.2f} which is {percent:.2f}% of your income.")

def get_expense(name):
    #Gets input from the user.
    return float(input(f"What is your {name}?\n"))

# print statement that welcomes my user and tells what the program does
print("Hi, this is a financial calculator. It will ask you some questions to help you make good financial decisions")

# Get user inputs
income = get_expense("income")
rent = get_expense("rent")
utilities = get_expense("utilities")
groceries = get_expense("groceries")
transportation = get_expense("transportation")

# calculate savings as 10% income (income*.1) (variable)
savings = income*.1
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = income-savings-rent-utilities-groceries-transportation


info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")
