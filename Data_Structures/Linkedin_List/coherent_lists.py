class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def search(self, target):
        
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    
    def delete(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = slow.next
                fast = fast.next.next

                if slow is fast:
                    return True
            except:
                return False


    def __str__(self):
        result = ""
        node = self.head
        while node is not None:
            if hasattr(node, 'data') and hasattr(node, 'next'):
                result += str(node.data) + " "
                node = node.next
            else:
                 result += "? "  # или что-то еще, чтобы указать отсутствие данных
        return result.strip()

def main():
    a_list = LinkedList()
    a_list.append("Monday")
    a_list.append("Tuesday")
    a_list.append("Wednesday")
    a_list.append("Thursday")
    a_list.append("Friday")
    a_list.append("Saturday")
    a_list.append("Sunday")
    print(a_list)
    print(a_list.search("Monday"))
    print(a_list.search("Day"))
    a_list.append(623)
    print(a_list)
    a_list.delete(623)
    print(a_list)
    #a_list.reverse_list()
    #print(a_list)
   

if __name__ == "__main__":
    main()
""" Практикум
1. Создайте связный список, содержащий числа от 1 до 100. Затем выведите
каждый узел списка.
2. Создайте два связных списка: один содержащий цикл, а другой — без цикла.
Убедитесь, что в каждом из них есть метод detect_cycle для определения
того, имеется ли в списке цикл. Вызовите detect_cycle для обоих списков """