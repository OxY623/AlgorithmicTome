class BinaryTreeNode:
    def __init__(self, value):
        """
        Класс для узла бинарного дерева.

        Параметры:
        - value: Значение узла.
        - left: Ссылка на левого потомка.
        - right: Ссылка на правого потомка.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        """
        Класс для бинарного дерева.

        Параметры:
        - root_value: Значение корневого узла.
        """
        self.root = BinaryTreeNode(root_value)

    def has_leaf_nodes(self):
        """
        Метод для проверки наличия узлов без листьев в дереве.

        Возвращает:
        - True, если есть узлы без листьев.
        - False, если все узлы являются листьями.
        """
        def _has_leaf_nodes(node):
            """
            Вспомогательная рекурсивная функция для проверки наличия узлов без листьев.

            Параметры:
            - node: Текущий узел, с которого начинается проверка.

            Возвращает:
            - True, если узел или его потомки имеют узлы без листьев.
            - False, если все узлы являются листьями.
            """
            if node is None:
                return False  # Если узла нет, значит листов тоже нет

            # Проверка, есть ли у текущего узла листья
            has_left_leaf_nodes = _has_leaf_nodes(node.left)
            has_right_leaf_nodes = _has_leaf_nodes(node.right)

            # Возвращаем True, если у текущего узла или его потомков есть узлы без листьев
            return has_left_leaf_nodes or has_right_leaf_nodes or (node.left is not None) or (node.right is not None)

        # Начинаем проверку с корневого узла
        return _has_leaf_nodes(self.root)

# Пример использования
if __name__ == "__main__":
    # Создаем дерево:        1
    #                     /   \
    #                    2     3
    #                   / \   / \
    #                  4   6 5   7
    tree = BinaryTree(1)
    tree.root.left = BinaryTreeNode(2)
    tree.root.right = BinaryTreeNode(3)
    tree.root.left.left = BinaryTreeNode(4)
    tree.root.left.right = BinaryTreeNode(5)
    tree.root.right.left = BinaryTreeNode(6)
    tree.root.right.right = BinaryTreeNode(7)
    

    # Проверяем наличие узлов без листьев
    has_leaf_nodes = tree.has_leaf_nodes()
    print("Дерево содержит узлы без листьев: ", has_leaf_nodes)
