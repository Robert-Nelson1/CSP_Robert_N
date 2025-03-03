#Robert Nelson, Loops Notes Python

#1.What is a loop? 
    #A section of code that repeats multiple times
#2.What are the two types of loops?
    #for loop
nums = [1,1,2,3,5,8,13,21,34]

for num in nums:
    print(num)
    #while loop

x = 0

while x < 10:
    print(x)
    x+= 1
#3.What is iteration
    #That specific instance of the loop
    #iteration the amount of times you are looping through
#4.What are lists?
    # A list is just a variable that holds multiple values?
nums = [1,2,3,4,5,6,7]
siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Hailey"]
print(nums) #prints while list, which is ugly
print(siblings[1]) #prints one item from the list

siblings[0] = "Jeremy" #renames user
print(siblings)

siblings.pop(0) #removes user
siblings.insert(0, "John")
print(siblings)
siblings.insert(1, "Gary")
#siblings.insert(2, "Joe", "Noah", "Zee")
#5.How do you make lists in python?
    #You use brackets, add in items with correct data types, and you have to have a comma between each item.
#6.How do you make for loops in python? 
for sibling in siblings:
    print(siblings)
for x in range(1, 5): #range stops before the max number which is 5
    print(x)
#7.How do you make while loops in python?
import random
x = 1 #variable to keep count of iteration
goose = random.randint(1,20)


while x <= 20:
    if x == goose:
        print("Goose!")
        break # tells loop to stop
    else:
        print("Duck")
    #print(x)
    x+= 1

#continue moves on to the next iteration without finishing
#8.How do you make lists in C?
#9.How do you make for loops in C?
#10.How do you make while loops in C?