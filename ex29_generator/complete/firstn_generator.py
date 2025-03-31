# Example of a generator function that generates the first n numbers
# The use of yield makes this a generator function
def firstn(n):
    # TODO
    num = 0
    while num < n:
        yield num
        num += 1

# Get the type of the generator
print()
print("type(firstn(5)):")
print(type(firstn(5)))

# Use a for loop to iterate over the generator
print()
print("for loop:")
for i in firstn(5):
    print(i)

# Convert the generator to a list
print()
print("Converting generator to list:")
lst = list(firstn(5))
print(lst)

# Take the sum of the generator
print()
print("Find the sum of a generator:")
sum_of_first_n = sum(firstn(10))
print(sum_of_first_n)

# Use next to iterate over the generator
print()
print("Using a while loop with next:")
it = iter(firstn(5))
print(type(it))  # <class 'generator'>
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# Once the generator has been exhausted, it can't be reused
print()
print("Calling next after exhaustion:")
try:
    print(next(it))
except StopIteration:
    print("No more items")

# Limit the number of items in a generator
print()
print("Using a for loop with break to limit to n items")
n = 5
gen = firstn(100)
for i, value in enumerate(gen):
    if i >= n:
        break
    print(value)

# Use islice to limit the number of items in a generator
print()
print("Using islice to limit to n items")
from itertools import islice
n = 5
gen = firstn(100)
for value in islice(gen, n):
    print(value)

# Generator expression, similar to list comprehension, 
# but returns a generator object
print()
print("Generator expression:")
squares = (x * x for x in range(5))
print(next(squares))
print(next(squares))
