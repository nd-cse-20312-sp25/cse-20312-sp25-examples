#!/usr/bin/env python3

# Adding two numbers
x = 5
y = 10
z = x + y
print(z)

# Adding two strings
x = "Hello"
y = "World"
z = x + " " + y
print(z)

# Formatting strings (f-strings)
x = 75
y = 25
z = f"The sum of {x} and {y} is {x + y}"
print(z)

# While loop and if statement
x = 0
while x < 5:
    if x % 2 == 0:
        print(x)
    x += 1

# For loop
# Note: range(5) only goes up to 4
for x in range(5):
    if x % 2 == 0:
        print(x)

# list
x = [100, 200, 300, 400, 500]
x.append(600)
x[2] = 350

# for loop with list
for y in x:
    print(y)

# slicing a list
# Note: x[1:3] only includes elements at index 1 and 2
y = x[1:3]
print(y)

y = x.pop(0)
print(y)

# dictionary
x = {"a": 100, "b": 200, "c": 300}
x["d"] = 400
x["a"] = 150
if ("a" in x):
    print("Key 'a' exists")

# set
x = set()
x.add(100)
x.add(200)
x.add(300)
x.remove(200)
print(x)

