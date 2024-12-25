#!/usr/bin/env python3

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinaryTree:
    # Constructor
    # Optionally, you can initialize the tree with a root node
    def __init__(self, root=None):
        self.root = root

    # Depth first search: preorder traversal
    def dfs(self):
        frontier_stack = [self.root]
        visited_list = []
        while frontier_stack:
            current = frontier_stack.pop()
            if current is not None:
                visited_list.append(current.key)
                frontier_stack.append(current.right)
                frontier_stack.append(current.left)
        return visited_list
    
    # Breadth first search: level order traversal
    def bfs(self):
        frontier_queue = [self.root]
        visited_list = []
        while frontier_queue:
            current = frontier_queue.pop(0)
            if current is not None:
                visited_list.append(current.key)
                frontier_queue.append(current.left)
                frontier_queue.append(current.right)
        return visited_list
    
if __name__ == "__main__":

    # Create a binary tree
    #     __1__
    #    /     \
    #   2       3
    #  / \     / \
    # 4   5   6   7

    root = Node(1)
    root.left =  Node(2)
    root.right = Node(3)
    root.left.left =   Node(4)
    root.left.right =  Node(5)
    root.right.left =  Node(6)
    root.right.right = Node(7)
    bt = BinaryTree(root)

    print("Depth-first search:")
    print(bt.dfs())
    print()
    print("Breadth-first search:")
    print(bt.bfs())
    print()
