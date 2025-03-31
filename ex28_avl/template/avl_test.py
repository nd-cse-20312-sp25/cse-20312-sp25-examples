#!/usr/bin/env python3

import unittest
from avl import AVLTree, Node

class AvlTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_init(self):
        avl = AVLTree()
        self.assertIsNone(avl.root)

    def test_init_with_root(self):
        root = Node(10)
        avl = AVLTree(root)
        self.assertEqual(avl.root, root)

    def test_get_height(self):
        avl = AVLTree()
        self.assertEqual(avl._get_height(avl.root), -1)

    def test_update_height(self):
        root = Node(20)
        avl = AVLTree(root)
        avl._update_height(avl.root)
        self.assertEqual(avl._get_height(avl.root), 0)
        root.left = Node(10)
        avl._update_height(avl.root)
        self.assertEqual(avl._get_height(avl.root), 1)
        root.right = Node(30)
        avl._update_height(avl.root)
        self.assertEqual(avl._get_height(avl.root), 1)
        root.left = None
        avl._update_height(avl.root)
        self.assertEqual(avl._get_height(avl.root), 1)

    def test_balance_factor(self):
        root = Node(20)
        avl = AVLTree(root)
        avl._update_height(avl.root)
        self.assertEqual(avl._balance_factor(avl.root), 0)
        root.left = Node(10)
        avl._update_height(avl.root)
        self.assertEqual(avl._balance_factor(avl.root), 1)
        root.right = Node(30)
        avl._update_height(avl.root)
        self.assertEqual(avl._balance_factor(avl.root), 0)
        root.left = None
        avl._update_height(avl.root)
        self.assertEqual(avl._balance_factor(avl.root), -1)

    def test_rotate_left(self):
        # General case
        root = Node(4)
        root.left =  Node(2)
        root.right = Node(6)
        root.right.left =  Node(5)
        root.right.right = Node(7)
        avl = AVLTree(root)
        avl.root = avl._rotate_left(avl.root)
        self.assertEqual(avl.write_bfs(), [6, 4, 7, 2, 5])
        # Right-right case
        root = Node(1)
        root.right = Node(2)
        root.right.right = Node(3)
        avl = AVLTree(root)
        avl.root = avl._rotate_left(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])

    def test_rotate_right(self):
        # General case
        root = Node(4)
        root.left =  Node(2)
        root.right = Node(6)
        root.left.left =  Node(1)
        root.left.right = Node(3)
        avl = AVLTree(root)
        avl.root = avl._rotate_right(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 4, None, None, 3, 6])
        # Left-left case
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        avl = AVLTree(root)
        avl.root = avl._rotate_right(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])

    def test_balance(self):
        # Left-left case
        #     3
        #    /
        #   2
        #  /
        # 1
        root = Node(3)
        root.height = 2
        root.left = Node(2)
        root.left.height = 1
        root.left.left = Node(1)
        avl = AVLTree(root)
        avl.root = avl._balance(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])

        # Left-right case
        #   __3
        #  /
        # 1
        #  \
        #   2
        root = Node(3)
        root.height = 2
        root.left = Node(1)
        root.left.height = 1
        root.left.right = Node(2)
        avl = AVLTree(root)
        avl.root = avl._balance(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])

        # Right-right case
        # 1
        #  \
        #   2
        #    \
        #     3
        root = Node(1)
        root.height
        root.right = Node(2)
        root.right.height = 1
        root.right.right = Node(3)
        avl = AVLTree(root)
        avl.root = avl._balance(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])

        # Right-left case
        # 1__
        #    \
        #     3
        #    /
        #   2
        root = Node(1)
        root.height = 2
        root.right = Node(3)
        root.right.height = 1
        root.right.left = Node(2)
        avl = AVLTree(root)
        avl.root = avl._balance(avl.root)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])

    def test_insert(self):
        avl = AVLTree()
        avl.insert(30)
        self.assertEqual(avl.root.key, 30)
        self.assertIsNone(avl.root.left)
        self.assertIsNone(avl.root.right)
        avl.insert(30)
        self.assertEqual(avl.root.key, 30)
        self.assertIsNone(avl.root.left)
        self.assertIsNone(avl.root.right)
        avl.insert(10)
        self.assertEqual(avl.root.left.key, 10)
        avl.insert(50)
        self.assertEqual(avl.root.right.key, 50)
        avl.insert(20)
        self.assertEqual(avl.root.left.right.key, 20)
        avl.insert(40)
        self.assertEqual(avl.root.right.left.key, 40)
        avl.insert(70)
        self.assertEqual(avl.root.right.right.key, 70)
        avl.insert(60)
        self.assertEqual(avl.root.right.right.left.key, 60)
        avl.clear()
        avl.insert(1)
        avl.insert(2)
        avl.insert(3)
        self.assertEqual(avl.write_bfs(), [2, 1, 3])
        avl.insert(4)
        avl.insert(5)
        avl.insert(6)
        self.assertEqual(avl.write_bfs(), [4, 2, 5, 1, 3, None, 6])
        avl.clear()
        avl.insert(6)
        avl.insert(5)
        avl.insert(4)
        self.assertEqual(avl.write_bfs(), [5, 4, 6])
        avl.insert(3)
        avl.insert(2)
        avl.insert(1)
        self.assertEqual(avl.write_bfs(), [3, 2, 5, 1, None, 4, 6])
    
    def test_min_value_node(self):
        avl = AVLTree()
        avl.insert(3)
        self.assertEqual(avl._min_value_node(avl.root), 3)
        avl.insert(2)
        self.assertEqual(avl._min_value_node(avl.root), 2)
        avl.insert(1)
        self.assertEqual(avl._min_value_node(avl.root), 1)

    def test_remove(self):
        avl = AVLTree()
        avl.insert(2)
        avl.remove(2)
        self.assertEqual(avl.root, None)
        avl.insert(2)
        avl.insert(1)
        avl.insert(3)
        avl.remove(1)
        self.assertEqual(avl.root.left, None)
        self.assertEqual(avl.root.right.key, 3)
        avl.remove(3)
        self.assertEqual(avl.root.right, None)
        avl.insert(3)
        avl.remove(2)
        self.assertEqual(avl.root.key, 3)
        avl.clear()
        avl.insert(30)
        avl.insert(10)
        avl.insert(50)
        avl.insert(40)
        avl.insert(45)
        avl.remove(30)
        self.assertEqual(avl.root.key, 40)
        self.assertEqual(avl.root.right.key, 45)
        self.assertEqual(avl.root.right.left, None)
        self.assertEqual(avl.root.right.right.key, 50)
        avl.clear()
        # Check rebalancing resulting from remove
        # Case: Right-Right
        avl.insert(40)
        avl.insert(20)
        avl.insert(60)
        avl.insert(70)
        avl.remove(20)
        self.assertEqual(avl.root.key, 60)
        self.assertEqual(avl.root.left.key, 40)
        self.assertEqual(avl.root.right.key, 70)
        avl.clear()
        # Case: Right-Left
        avl.insert(40)
        avl.insert(20)
        avl.insert(60)
        avl.insert(55)
        avl.remove(20)
        self.assertEqual(avl.root.key, 55)
        self.assertEqual(avl.root.left.key, 40)
        self.assertEqual(avl.root.right.key, 60)

    def test_write_bfs(self):
        avl = AVLTree()
        avl.insert(30)
        self.assertEqual(avl.write_bfs(), [30])
        avl.insert(50)
        self.assertEqual(avl.write_bfs(), [30, None, 50])
        avl.insert(10)
        self.assertEqual(avl.write_bfs(), [30, 10, 50])
        avl.insert(20)
        avl.insert(40)
        avl.insert(70)
        self.assertEqual(avl.write_bfs(), [30, 10, 50, None, 20, 40, 70])
        avl.insert(60)
        self.assertEqual(avl.write_bfs(), [30, 10, 50, None, 20, 40, 70, None, None, None, None, 60])

if __name__ == '__main__':
    unittest.main()
