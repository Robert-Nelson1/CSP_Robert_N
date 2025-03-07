# Robert Nelson, FizzBuzz - Python
x = 1
for x in range(1, 51, 1): #range stops before the max number which is 5
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)