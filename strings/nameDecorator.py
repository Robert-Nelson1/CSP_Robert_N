# Robert Nelson, Name Decorator - Python

name = input("What is your first name?\n").strip().lower().capitalize()

smiley ="(: (: (: "
moreSmiley = " :) :) :)"
newString = smiley + name + moreSmiley
print(f"Hello {newString}, welcome to my program!")