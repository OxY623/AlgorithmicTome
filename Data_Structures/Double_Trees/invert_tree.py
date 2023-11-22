class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    """
    Инвертирование двоичного дерева с использованием обхода в глубину.

    Параметры:
    - root: Корень двоичного дерева.

    Возвращает:
    - Инвертированное двоичное дерево.
    """
    if root is None:
        return None

    # Рекурсивно инвертируем левое и правое поддеревья
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)

    return root

def print_tree(root):
    """
    Вспомогательная функция для вывода значений узлов в порядке обхода в глубину.

    Параметры:
    - root: Корень двоичного дерева.
    """
    if root is not None:
        print(root.value, end=" ")
        print_tree(root.left)
        print_tree(root.right)

# Пример использования
if __name__ == "__main__":
    # Создаем дерево:        1
    #                     /   \
    #                    2     3
    #                   / \
    #                  4   5
    original_tree = TreeNode(1)
    original_tree.left = TreeNode(2)
    original_tree.right = TreeNode(3)
    original_tree.left.left = TreeNode(4)
    original_tree.left.right = TreeNode(5)

    print("Исходное дерево:")
    print_tree(original_tree)

    # Инвертируем дерево
    inverted_tree = invert_tree(original_tree)

    print("\nИнвертированное дерево:")
    print_tree(inverted_tree)
