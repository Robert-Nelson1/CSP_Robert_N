#Robert Nelson, Old Enough- Python

name = input("What is your name?\n")

if name == "Robert":
    print("Hi Robert!")
else:
    print(f"Hello {name}!")


num = int(input("How old are you?\n"))
#computers read top to bottom, check the least likely first
if num == 0: #<= if always starts the conditional
    print("How can you type at 0?")
elif num >=18: #<= everything in between should be elif
    print("You can vote.")
elif num >=16:
    print("You can drive.")
elif num >=15:
    print("You can get a learners permit.")
elif num >=5:
    print("You can go to school.")
else: #<= else always ends the conditional
    print("You can't vote, drive, get a learners permit, and go to school.")
