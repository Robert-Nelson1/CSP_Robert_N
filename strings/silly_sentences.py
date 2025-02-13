# Robert Nelson, silly sentences C

# empty string variables for user words (minimum 3)


# A welcome for the user telling them what the program is (print)
print("Hello, this program is going to make a silly sentence and is going to ask you easy questions.")
name = input("What is your name: \n").strip().lower().capitalize()
    
#ask user for words (print statement with a question scanf to set to) (in C we need to tell the user we can only write one word.)
adjective = input("Give me an verb!: \n").strip().lower()

noun = input("Give me an noun!:\n").strip().lower()

#print out story with the variables inserted ("welcome %s to my program", name)
print("You,", name, "will", adjective, "to your", noun)

