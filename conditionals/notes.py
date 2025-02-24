#Robert Nelson, Conditional notes Python
name = input("what is your name")
#What puts something inside of the “if” statement? Whatever is in the whitespace, or called the tab
if name == "Robert":
    print("Hi Robert")
#
# 2. What do if statements do?
#Checks a conditions and if it is true it will do a thing
if name == "Robert": #<= this is the condtion
    print("Hi Robert") #<=This is what it does if true.
else: #This happens if the condition is false
    print(f"Hello {name}!")
# 3. What are boolean statements?
#       True or False statements

if name == "Robert": #<= this is the boolean statement, it either true or false.
    print("Hi Robert") #<=This is what it does if true.
else: #This happens if the condition is false
    print(f"Hello {name}!")


#4. What do else statements do?

if name == "Robert": 
    print("Hi Robert") 
else: #If the boolean is false, the else statement happens
    print(f"Hello {name}!")

# 5. What kind of statement do you use if you have more than 2 needed outcomes?

num = int(input("How many cookies are there?\n"))
#computers read top to bottom, check the least likely first
if num == 0: #<= if always starts the condtional
    print("There are none.")
elif num == 1: #<= everything in between should be elif
    print("There is one")
elif num <4:
    print("There is a couple")
elif num <10:
    print("There is a few")
else: #<= else always ends the condtional
    print("There are many")
# 6. What do each of the different symbols mean in conditionals?
#< less than
#> greater than
#<= less than or equal to
#>= greater than or equal to
#== Equal to
#=== *Doesn't exist in Python*
#! Not
# 7. What are the 3 logical operators?
if num <10 and num >5: #and, both booleans must be true
    print("This is a big single digit number")

if num <10 or num >5: #or, one booleans must be true
    print("This is a single digit number")

if not num <10: #not changes to check if false
    print("This is a not single digit number")
# 8. What are logical operators for?
    #Allows the code to handle more difficult questions and increases complexity

# 9. What does a nested conditional statement do? # put an if statement in a if statement
if num <10:
    if num ==8:
        print("This prints at 8")
    else:
        print("The number is the less than 10")
#else:
 #   print("The humber is biger than 10")
#How do you write an if statement in C?
#How do you write else statements in C?
#How do you write elif/ else if statements in C?
#How do you write the 3 logical operators in C?