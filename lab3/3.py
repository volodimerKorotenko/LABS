# Класс AVL-дерева (1)
class Node:
    def __init__(self, key):
        self.key = key  # Значення вузла
        self.left = None  # Лівий насщадок
        self.right = None  # Правий насщадок
        self.height = 1  # Висота вузла

# Класс для створення AVL-дерева (1)
class AVLTree:
    # Отримаємо висоту вузла
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Обчислюємо баланс вузла(3)
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Правое обертання (4)
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2

        # Оновлення висоти
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    # Левое обертання (4)
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        # крок 1: Виконуємо звичайну вставку
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # крок 2: Оновлюємо висоту теперішнього вузла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # крок 3: Перевіряємо баланс вузла (5)
        balance = self.get_balance(root)

        # крок 4: Балансировка вузла
        # Левый-левый случай
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Правий-правий
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Левій-правий
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Правий-лівий
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Функция виводу дерева (в порядке зростання)
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(f"{root.key} (Height: {root.height})", end=" ")
            self.in_order_traversal(root.right)


# Передивляємося результат
if __name__ == "__main__":
    avl = AVLTree()
    root = None    
    keys = [10, 20, 16, 99, 52, 87, 12, 77, 66, 932, 0, 40, 50, 25]
    for key in keys:
        root = avl.insert(root, key)
    print("Обход AVL-дерева (In-order):")
    avl.in_order_traversal(root)
