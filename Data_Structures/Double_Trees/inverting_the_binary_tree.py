class BinaryTree:
    def __init__(self, value):
        # Конструктор класса, инициализирует узел дерева с заданным значением.
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        # Вставка узла слева от текущего узла.
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            # Если слева уже есть узел, то создаем новый узел и вставляем его перед существующим.
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        # Вставка узла справа от текущего узла.
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            # Если справа уже есть узел, то создаем новый узел и вставляем его перед существующим.
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def invert(self):
        # Инвертирование бинарного дерева (обмен значениями левого и правого поддеревьев).
        current = [self]  # Текущий уровень для обхода
        next_level = []   # Следующий уровень для обхода

        while current:
            for node in current:
                # Обмен значениями левого и правого поддеревьев у текущего узла.
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp

                # Добавляем дочерние узлы в следующий уровень для дальнейшего обхода.
                if node.left_child:
                    next_level.append(node.left_child)
                if node.right_child:
                    next_level.append(node.right_child)

            # Переходим к следующему уровню для обхода.
            current = next_level
            next_level = []
            
    def __str__(self):
            result = []  # List to store the node values in pre-order traversal
            stack = [self]  # Stack to perform iterative pre-order traversal

            while stack:
                node = stack.pop()
                if node:
                    result.append(str(node.key))
                    stack.append(node.right_child)
                    stack.append(node.left_child)
                else:
                    result.append("None")

            return " ".join(result)

# Пример использования:

# Создаем экземпляр дерева
tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)

# Выводим исходное дерево
print("Исходное дерево:")
print(tree)
# (Здесь вы можете вставить код для вывода дерева в удобном для вас формате)

# Инвертируем дерево
tree.invert()

# Выводим инвертированное дерево
print("\nИнвертированное дерево:")
# (Здесь вы можете вставить код для вывода инвертированного дерева в удобном для вас формате)
print(tree)
