class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        return self.recursive_function(self.head)
    
    # Function recursively returns a string representation of the linked list
    def recursive_function(self, current):
        # TODO
        if not current:
            return ''
        
        return str(current.data) + ' ' + self.recursive_function(current.next)

    def __iter__(self):
        # TODO
        self.current = self.head
        return self

    def __next__(self):
        # TODO
        if not self.current:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

# ---- Example usage ----
        
# Create a linked list and append some elements
lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)

# Print the type of the linked list
print("Print using __str__:")
print(f"type(lst.__str__()): {type(lst.__str__())}")
print(lst)

# Iterate over the linked list using a for loop
print()
print("Iterate using for loop:")
# TODO
for i in lst:
    print(i)

# Iterate over the linked list using a while loop and generator
print()
print("Iterate using while loop and generator:")
# TODO
iterator = iter(lst)
print(f"type(iterator): {type(iterator)}")
# TODO
while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("End of list")
        break

# Convert the linked list to a list
print()
print("Convert iterable to list: list(lst)")
# TODO
print(list(lst))

