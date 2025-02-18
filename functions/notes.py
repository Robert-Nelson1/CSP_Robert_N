# Robert Nelson, Functions Notes Python
"""*/

def add():
    numOne = int(input("Please give me a number:\n"))
    numTwo = int(input("Please give me another number:\n"))

    print(numOne+numTwo)

add()
add()
add()



/*""""""
def add():

    number = int(input("Please give me a number:\n"))

#def add(numOne, numTwo):#parameters set the name of the variable (just fot eh function)
 #   print(numOne+numTwo)

add(number, 21)#arguements set the value of the variable just for that instance of the function
addition = add(6,4)
add(addition, 1)
add()
add()"""
"""
def values(type):
    return input(f"please give me a {type}:\n")
name = values("name")
print(f"{name} was really fast")
"""
def temp():
    celcius = int(input("What tempretaure is it outside in Farenheit for you right now?"))
    print(celcius)
cool = temp(celcius, 32)