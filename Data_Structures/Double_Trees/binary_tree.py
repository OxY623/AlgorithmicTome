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

    def breadth_first_search(self, n):
        # Поиск в ширину, начиная с корня дерева.
        current = [self]  # Текущий уровень для обхода
        next_level = []  # Следующий уровень для обхода

        while current:
            for node in current:
                # Проверяем, содержит ли текущий узел искомое значение.
                if node.key == n:
                    return True

                # Добавляем дочерние узлы в следующий уровень для дальнейшего обхода.
                if node.left_child:
                    next_level.append(node.left_child)
                if node.right_child:
                    next_level.append(node.right_child)

            # Переходим к следующему уровню для обхода.
            current = next_level
            next_level = []

        # Если значение не найдено.
        return False


# Создание экземпляра дерева
tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)
tree.left_child.left_child.insert_left(7)
tree.left_child.left_child.insert_right(8)
tree.right_child.right_child.insert_left(9)

# Поиск значений 9 и 11 в дереве
results = list(map(tree.breadth_first_search, [9, 11]))
print(results)

#Прямой обход дерева в глубинy
def preorder(tree):
 if tree:
    print(tree.key)
    preorder(tree.left_child)
    preorder(tree.right_child)

#Обратный обход дерева в глубину
def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)
#Симметричный обход дерева в глубинy
def inorder(tree):
    if tree:
        inorder (tree.left_child)
        print(tree.key)
        inorder (tree.right_child)

preorder(tree)