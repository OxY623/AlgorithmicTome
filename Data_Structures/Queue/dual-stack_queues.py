class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enqueue(self, item):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1)==0:
            raise Exception("Cannot pop from empty queue")
        return self.s1.pop()

    def __str__(self):
        str_a = ""
        for i in self.s1:
            str_a = str_a + str(i) + ", "
        return str_a[:-2]
            

queue1 = Queue()
queue1.enqueue(1)
for i in range(2,10):
    queue1.enqueue(i)
print(queue1)
for i in range(1,10,2):
    queue1.dequeue()
print(queue1)

