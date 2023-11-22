import time

class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

def create_linked_list(start, end):
    head = Node(start)
    current = head
    for i in range(start + 1, end + 1):
        current.next = Node(i)
        current = current.next
    return head

def create_linked_list_with_cycle(start, end, cycle_start):
    head = Node(start)
    current = head
    cycle_node = None

    for i in range(start + 1, end + 1):
        current.next = Node(i)
        current = current.next
         # Если текущий узел соответствует месту, где должен начаться цикл
        if i == cycle_start:
            cycle_node = current
        

   # Устанавливаем указатель последнего узла на узел, с которого начинается цикл
    current.next = cycle_node

    return head


def print_linked_list(head):
    current = head
    start_time = time.time()
    while current:
        print(current.data, end=" --> ")
        current = current.next
        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            print("Превышено время выполнения (более 10 секунд). Прекращаем цикл.")
            break
        
    print("None")


def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Создание связанного списка с циклом (цикл начинается с узла 50)
linked_list_with_cycle = create_linked_list_with_cycle(1, 100, 50)
# Создание связанного списка без цикла
linked_list_without_cycle = create_linked_list(1, 100)
# Проверка для обоих списков
print("Связанный список c циклом:")
print_linked_list(linked_list_with_cycle)
print("Цикл в списке:", detect_cycle(linked_list_with_cycle))

print("\nCвязaный список без цикла:")
print_linked_list(linked_list_without_cycle)
print("Цикл в списке:", detect_cycle(linked_list_without_cycle))



