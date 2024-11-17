class Node:
    """Класс для узла дерева"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Класс для бинарного дерева поиска"""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставка элемента в дерево"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        """Поиск элемента в дереве"""
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def delete(self, key):
        """Удаление элемента из дерева"""
        self.root = self._delete(self.root, key)

    def _delete(self, current, key):
        if current is None:
            return current
        if key < current.key:
            current.left = self._delete(current.left, key)
        elif key > current.key:
            current.right = self._delete(current.right, key)
        else:
            # Узел с одним или без потомков
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Узел с двумя потомками
            min_larger_node = self._find_min(current.right)
            current.key = min_larger_node.key
            current.right = self._delete(current.right, min_larger_node.key)
        return current

    def _find_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Симметричный обход дерева"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current is not None:
            self._inorder(current.left, result)
            result.append(current.key)
            self._inorder(current.right, result)

# Пример использования
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)

    print("Симметричный обход дерева:", bst.inorder())

    print("Поиск 7:", "Найдено" if bst.search(7) else "Не найдено")
    print("Поиск 20:", "Найдено" if bst.search(20) else "Не найдено")

    bst.delete(10)
    print("Симметричный обход после удаления 10:", bst.inorder())