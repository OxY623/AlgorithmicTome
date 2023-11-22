class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def is_empty(self):
        if len(self.main) == 0:
            return True
        return False
    
    def push(self, value):
        self.main.append(value)

        # Если max_stack пуст или новое значение больше текущего максимального,
        # то добавляем новое значение в max_stack, иначе добавляем текущий максимум
        if not self.max or value > self.max[-1]:
            self.max.append(value)
        else:
            self.max.append(self.max[-1])

    def pop(self):
        self.max.pop()
        return self.main.pop()
    
    def __str__(self):
        str_a=""
        for i in range(0,len(self.main)):
            str_a=str_a + str(self.main[i])+ ","
        str_a = str_a + " max: " + str(self.max[-1])
        return str_a
    
stack = MaxStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
stack.push(0)
stack.push(99)
print(stack)
stack.pop()
print(stack)