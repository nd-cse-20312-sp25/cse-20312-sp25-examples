#!/usr/bin/env python3

import unittest
from bst import BSTree, Node

class BstTest(unittest.TestCase):
    '''
    Sample tree used in many of the tests

     ____30___
    /         \
   10         _50___
     \       /      \
      20    40      _70
                   /
                  60
    '''
    sample_bst = BSTree(Node(
                30, 
                Node(
                    10, 
                    None,
                    Node(20)),
                Node(
                    50, 
                    Node(40), 
                    Node(
                        70, 
                        Node(60), 
                        None))))
    
    sample_bfs = [30, 10, 50, None, 20, 40, 70, None, None, None, None, 60]

    def test_init(self):
        bst = BSTree()
        self.assertIsNone(bst.root)

    def test_init_with_root(self):
        root = Node(10)
        bst = BSTree(root)
        self.assertEqual(bst.root, root)

    def test_insert(self):
        bst = BSTree()
        bst.insert(30)
        self.assertEqual(bst.root.key, 30)
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)
        bst.insert(30)
        self.assertEqual(bst.root.key, 30)
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)
        bst.insert(10)
        self.assertEqual(bst.root.left.key, 10)
        bst.insert(50)
        self.assertEqual(bst.root.right.key, 50)
        bst.insert(20)
        self.assertEqual(bst.root.left.right.key, 20)
        bst.insert(40)
        self.assertEqual(bst.root.right.left.key, 40)
        bst.insert(70)
        self.assertEqual(bst.root.right.right.key, 70)
        bst.insert(60)
        self.assertEqual(bst.root.right.right.left.key, 60)

    def test_contains(self):
        bst = BSTree()
        bst.insert(30)
        self.assertTrue(30 in bst)
        bst.insert(10)
        self.assertTrue(10 in bst)
        bst.insert(50)
        self.assertTrue(50 in bst)
        bst.insert(20)
        self.assertTrue(20 in bst)
        bst.insert(40)
        self.assertTrue(40 in bst)
        bst.insert(70)
        self.assertTrue(70 in bst)
        bst.insert(60)
        self.assertTrue(60 in bst)
        self.assertFalse(0 in bst)
        self.assertFalse(100 in bst)

    def test_inorder(self):
        bst = BSTree()
        self.assertEqual(bst.inorder(), [])
        bst.insert(30)
        self.assertEqual(bst.inorder(), [30])
        bst.insert(10)
        self.assertEqual(bst.inorder(), [10, 30])
        bst.insert(50)
        self.assertEqual(bst.inorder(), [10, 30, 50])
        bst.insert(20)
        self.assertEqual(bst.inorder(), [10, 20, 30, 50])
        bst.insert(40)
        self.assertEqual(bst.inorder(), [10, 20, 30, 40, 50])
        bst.insert(70)
        self.assertEqual(bst.inorder(), [10, 20, 30, 40, 50, 70])
        bst.insert(60)
        self.assertEqual(bst.inorder(), [10, 20, 30, 40, 50, 60, 70])

    def test_len(self):
        bst = BSTree()
        self.assertEqual(len(bst), 0)
        bst.insert(30)
        self.assertEqual(len(bst), 1)
        bst.insert(10)
        self.assertEqual(len(bst), 2)
        bst.insert(50)
        self.assertEqual(len(bst), 3)
        bst.insert(20)
        self.assertEqual(len(bst), 4)
        bst.insert(40)
        self.assertEqual(len(bst), 5)
        bst.insert(70)
        self.assertEqual(len(bst), 6)
        bst.insert(60)
        self.assertEqual(len(bst), 7)

    def test_height(self):
        bst = BSTree()
        self.assertEqual(bst.height(), -1)
        bst.insert(30)
        self.assertEqual(bst.height(), 0)
        bst.insert(10)
        self.assertEqual(bst.height(), 1)
        bst.insert(50)
        self.assertEqual(bst.height(), 1)
        bst.insert(20)
        self.assertEqual(bst.height(), 2)
        bst.insert(40)
        self.assertEqual(bst.height(), 2)
        bst.insert(70)
        self.assertEqual(bst.height(), 2)
        bst.insert(60)
        self.assertEqual(bst.height(), 3)
    
    def test_min_value_node(self):
        bst = BSTree()
        bst.insert(3)
        self.assertEqual(bst._min_value_node(bst.root), 3)
        bst.insert(2)
        self.assertEqual(bst._min_value_node(bst.root), 2)
        bst.insert(1)
        self.assertEqual(bst._min_value_node(bst.root), 1)

    def test_remove(self):
        bst = BSTree()
        bst.insert(2)
        bst.remove(2)
        self.assertEqual(bst.root, None)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.remove(1)
        self.assertEqual(bst.root.left, None)
        self.assertEqual(bst.root.right.key, 3)
        bst.remove(3)
        self.assertEqual(bst.root.right, None)
        bst.insert(3)
        bst.remove(2)
        self.assertEqual(bst.root.key, 3)
        bst.clear()
        bst.insert(30)
        bst.insert(10)
        bst.insert(50)
        bst.insert(40)
        bst.insert(45)
        bst.remove(30)
        self.assertEqual(bst.root.key, 40)
        self.assertEqual(bst.root.right.key, 50)
        self.assertEqual(bst.root.right.left.key, 45)

    def test_write_bfs(self):
        bst = BSTree()
        bst.insert(30)
        self.assertEqual(bst.write_bfs(), [30])
        bst.insert(50)
        self.assertEqual(bst.write_bfs(), [30, None, 50])
        bst.insert(10)
        self.assertEqual(bst.write_bfs(), [30, 10, 50])
        bst.insert(20)
        bst.insert(40)
        bst.insert(70)
        self.assertEqual(bst.write_bfs(), [30, 10, 50, None, 20, 40, 70])
        bst.insert(60)
        self.assertEqual(bst.write_bfs(), [30, 10, 50, None, 20, 40, 70, None, None, None, None, 60])

if __name__ == '__main__':
    unittest.main()
