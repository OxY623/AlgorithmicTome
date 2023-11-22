class MinStack:

    def __init__(self):
        self.main = []
        self.min = []

    def push(self, data):
        if len(self.main) == 0:
            self.min.append(data)
        elif data <= self.min[-1]:
            self.min.append(data)
        else:
            self.min.append(self.min[-1])
        self.main.append(data)
    
    def pop(self):
        self.min.pop()
        return self.main.pop()
    
    def get_min(self):
        return self.min[-1]
    
    def __str__(self):
        str_a=""
        for i in range(0,len(self.main)):
            str_a = str_a + str(self.main[i]) + ", "
        str_a+= ("min is : " + str(self.min[-1]))
        return str_a
    
stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
stack.push(-3)
print(stack)
print(stack.main)
print(stack.min)