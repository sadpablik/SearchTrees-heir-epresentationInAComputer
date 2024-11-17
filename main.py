class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка элемента в дерево
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    # Поиск элемента в дереве
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node, key):
        if current_node is None or current_node.key == key:
            return current_node
        if key < current_node.key:
            return self._search(current_node.left, key)
        return self._search(current_node.right, key)

    # Удаление элемента из дерева
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел найден, нужно удалить
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Узел с двумя потомками: получить преемника
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Симметричный обход дерева (в порядке возрастания)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# Пример использования дерева
if __name__ == "__main__":
    # Создаем дерево поиска
    bst = BinarySearchTree()
    
    # Вставляем элементы
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(5)
    bst.insert(15)
    
    # Печатаем отсортированные элементы (симметричный обход)
    print("Inorder traversal:", bst.inorder())
    
    # Ищем элементы
    print("Search for 15:", bst.search(15) is not None)
    print("Search for 40:", bst.search(40) is not None)
    
    # Удаляем элемент
    bst.delete(10)
    print("Inorder traversal after deleting 10:", bst.inorder())
