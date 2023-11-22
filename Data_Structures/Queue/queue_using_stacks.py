class  QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, data):
        self.stack_in.append(data)

    def dequeue(self):
        if not self.stack_out: 
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            return None
        
        return self.stack_out.pop()
    
# Пример использования
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Вывод: 1
print(queue.dequeue())  # Вывод: 2

queue.enqueue(4)
print(queue.dequeue())  # Вывод: 3
print(queue.dequeue())  # Вывод: 4