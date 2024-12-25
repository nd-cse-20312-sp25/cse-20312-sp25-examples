msg = "this is a string"
print(f'type of msg: {type(msg)}')
print()

print("Listing of string methods")
print(dir(msg))
print()

print("Call regular string methods upper() and split()")
print("msg.upper()")
print(msg.upper())
print()

print("msg.split()")
print(msg.split())
print()

print("The magic method __contains__() is called by the keyword 'in'")
print("msg.__contains__('r')")
print(msg.__contains__('r'))
print("'r' in msg")
print('r' in msg)
print("msg.__contains__('x')")
print(msg.__contains__('x'))
print("'x' in msg")
print('x' in msg)
print()

print("Try out your own examples below")
print()