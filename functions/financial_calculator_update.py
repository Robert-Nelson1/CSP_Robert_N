# Robert Nelson, Update your Financial Calculator - Python

def info(cost, income, type):
    percent = cost/income*100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")



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
#print("You should be saving 10% of your income which is $", savings)
# calculate spending as income-savings-rent-utilities-groceries-transportation (variable)
spending = income-savings-rent-utilities-groceries-transportation
#print("You should spend only $", spending, "otherwise you will go in debt")


info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")
