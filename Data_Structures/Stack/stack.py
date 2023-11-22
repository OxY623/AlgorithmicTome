class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data

    def __str__(self):
        str_a = ''
        current = self.head
        while current:
            str_a += str(current.data)
            current = current.next
            str_a += ', '
        return str_a[:-2]

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)   # Output: 3, 2, 1
print(stack.pop())  # Output: 3
print(stack)   # Output: 2, 1


# Simple Variant
#for i in range(3):
    #print(stack.pop())


# class Stack:

#     def __init__(self):
#         self.items = []

#     def push(self, data):
#         self.items.append(data)

#     def pop(self):
#         return self.items.pop()
    
#     def size(self):
#         return len(self.items)
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def peek(self):
#         return self.items[-1]
    
#     def __str__(self) -> str:
#         str_a = ''
#         for i in self.items:
#             str_a = str_a + ( str(i) + ' ')
#         return str_a            
    

