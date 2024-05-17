"""Реалізація двійкового дерева пошуку (BST)"""

class Node:
    def __init__(self, key):
        """Визначення класу вузла (Node)"""
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """Функція для вставки нового вузла"""
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_maximum(root):
    """Функція для знаходження найбільшого значення в BST"""
    current = root
    while current.right is not None:
        current = current.right
    return current.val

def find_minimum(root):
    """Функція для знаходження найменшого значення в BST"""
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def sum_values(root):
    """Функція для знаходження суми всіх значень у BST"""
    if root is None:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)



# Створення дерева та вставка елементів:
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Пошук значення
print("Найбільше значення у дереві:", find_maximum(root))
print("Найменше значення у дереві:", find_minimum(root))
print("Сума всіх значень у дереві:", sum_values(root))
