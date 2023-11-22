class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def is_min_heap(root):
    if root is None:
        return True
    
    # Рекурсивная функция для проверки свойства минимальной кучи
    def check_min_heap(node):
        # Базовый случай: если узел является листом, он удовлетворяет свойству
        if node.left is None and node.right is None:
            return True

        # Проверяем, что значение узла меньше или равно значения его дочерних узлов
        if node.left is not None and node.left.value < node.value:
            return False
        if node.right is not None and node.right.value < node.value:
            return False

        # Рекурсивно проверяем свойство для левого и правого поддеревьев
        return check_min_heap(node.left) and check_min_heap(node.right)

    # Начинаем проверку с корня дерева
    return check_min_heap(root)


# Пример использования:
# Создаем двоичное дерево
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)

# Проверяем, является ли дерево минимальной кучей
result = is_min_heap(root)

# Выводим результат
print(result)

    