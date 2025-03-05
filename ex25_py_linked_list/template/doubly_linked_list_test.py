#!/usr/bin/env python3

import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def test_insert_after(self):
        dll = DoublyLinkedList()       
        dll._insert_after(dll.head, 1)
        dll._insert_after(dll.head.next, 3)
        dll._insert_after(dll.head.next, 2)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.head.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.data, 3)

    def test_pop_node(self):
        dll = DoublyLinkedList()
        dll._insert_after(dll.head, 3)
        dll._insert_after(dll.head, 2)
        dll._insert_after(dll.head, 1)
        self.assertEqual(dll._pop_node(dll.head.next.next), 2)
        self.assertEqual(dll._pop_node(dll.tail.prev), 3)
        self.assertEqual(dll._pop_node(dll.head.next), 1)
        self.assertEqual(dll.head.next, dll.tail)
            
    def test_append(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.tail.prev.data, 2)

    def test_insert(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(3)
        dll.insert(1, 2)
        dll.insert(0, 0)
        dll.insert(4, 4)
        self.assertEqual(dll.head.next.data, 0)
        self.assertEqual(dll.head.next.next.data, 1)
        self.assertEqual(dll.head.next.next.next.data, 2)
        self.assertEqual(dll.head.next.next.next.next.data, 3)
        self.assertEqual(dll.tail.prev.data, 4)

    def test_pop(self):
        dll = DoublyLinkedList()
        for i in range(5):
            dll.append(i)
        self.assertEqual(dll.pop(2), 2)
        self.assertEqual(dll.pop(0), 0)
        self.assertEqual(dll.pop(2), 4)
        self.assertEqual(dll.head.next.data, 1)
        self.assertEqual(dll.tail.prev.data, 3)

    def test_clear(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.clear()
        self.assertEqual(dll.head.next, dll.tail)

    def test_index(self):
        dll = DoublyLinkedList()
        for i in range(5):
            dll.append(i)
        self.assertEqual(dll.index(0), 0)
        self.assertEqual(dll.index(3), 3)
        self.assertEqual(dll.index(4), 4)
        self.assertEqual(dll.index(5), -1)

    def test_str(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(str(dll), "1 2 3")

    def test_bool(self):
        dll = DoublyLinkedList()
        if dll:
            self.fail()
        dll.append(1)
        if not dll:
            self.fail()

    def test_contains(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        self.assertTrue(1 in dll)
        self.assertTrue(2 in dll)
        self.assertFalse(3 in dll)

    def test_iter_next(self):
        dll = DoublyLinkedList()
        for i in [1, 2, 3]:
            dll.append(i)
        lst = []
        for i in dll:
            lst.append(i)
        self.assertEqual(lst, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()