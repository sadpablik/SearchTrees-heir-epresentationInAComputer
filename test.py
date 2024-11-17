import unittest
from main import BinarySearchTree
# для запуска теста python -m unittest test

class TestBinarySearchTree(unittest.TestCase):
    
    # Тест на вставку и поиск элементов
    def test_insert_and_search(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        
        # Проверка, что элементы были вставлены
        self.assertIsNotNone(bst.search(20))
        self.assertIsNotNone(bst.search(10))
        self.assertIsNotNone(bst.search(30))
        
        # Проверка поиска несуществующего элемента
        self.assertIsNone(bst.search(40))

    # Тест на удаление узлов
    def test_delete(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        
        # Удаляем узел с одним потомком
        bst.delete(5)
        self.assertIsNone(bst.search(5))  # Убедиться, что 5 был удален
        
        # Удаляем узел с двумя потомками
        bst.delete(10)
        self.assertIsNone(bst.search(10))  # Убедиться, что 10 был удален
        
        # Удаляем узел с отсутствием потомков
        bst.delete(30)
        self.assertIsNone(bst.search(30))  # Убедиться, что 30 был удален
        
        # Проверим состояние дерева после удаления
        self.assertEqual(bst.inorder(), [15, 20])

    # Тест на симметричный обход
    def test_inorder(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(10)
        bst.insert(30)
        bst.insert(5)
        bst.insert(15)
        
        # Проверка симметричного обхода
        self.assertEqual(bst.inorder(), [5, 10, 15, 20, 30])

if __name__ == "__main__":
    unittest.main()
