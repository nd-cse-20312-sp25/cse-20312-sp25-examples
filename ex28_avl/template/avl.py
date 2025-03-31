from tree_print import pretty_tree

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 0

class AVLTree:
    # Constructor
    # Optionally, you can initialize the tree with a root node
    def __init__(self, root=None):
        self.root = root
    
    # Clear the tree
    def clear(self):
        self.root = None

    # Helper function to get the height of a node for AVL balancing
    # Note: The height of a null node is -1
    def _get_height(self, node):
        if not node:
            return -1
        return node.height
    
    # Helper function to update the height of a node
    def _update_height(self, node):
        # TODO
        pass
    
    # Helper function to get the balance factor of a node
    # Note: The balance factor of a null node is 0
    def _balance_factor(self, node):
        # TODO
        pass

    # Helper functions to rotate left for AVL balancing
    def _rotate_left(self, z):
        """
        Example:
            Given the following tree:
            z
           / \
          T1  y
             / \
            T2  T3

            After _left_rotate(z), the tree becomes:
              y
             / \
            z   T3
           / \
          T1  T2
        """
        # TODO
        # Do the rotation
        pass

        # Update the heights
        pass

        # Return the new root
        pass

    # Helper functions to rotate right for AVL balancing
    def _rotate_right(self, z):
        """
        Example:
            Given the following tree:
              z
             / \
            y  T3
           / \
          T1  T2

            After _right_rotate(z), the tree becomes:
              y
             / \
            T1  z
               / \
              T2  T3
        """
        # Do the rotation
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        # Update the heights
        self._update_height(z)
        self._update_height(y)

        # Return the new root
        return y

    def _balance(self, node):
        # TODO
        # update height
        pass

        # left heavy
        pass
            # left child is right heavy
        pass

        # right heavy
        pass
            # right child is left heavy
        pass

        return node

    # Insert a Node with a given key into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Helper function for insert
    def _insert(self, root, key):
        # Regular BST insertion
        if root is None:
            return Node(key)
        
        if key == root.key:
            return root
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        # TODO: Balance tree before returning
        return root
    
    # Remove a Node with a given key from the tree  
    def remove(self, key):
        self.root = self._remove(self.root, key)
    
    # Helper function for remove
    def _remove(self, root, key):
        # Regular BST removal
        if root is None:
            return root
        
        # Key is not yet found
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)

        # Key is found
        else:
            # Node with only one child or leaf node: return the non-null child
            # If the node has no children, return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value_node(root.right)
            # Delete the inorder successor
            root.right = self._remove(root.right, root.key)

        # TODO: Balance tree before returning
        return root
    
    # Helper function to find the minimum value node in a tree
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key
    
    # Write the BFS traversal of the tree to a list
    def write_bfs(self):
        # If the tree is empty, return an empty list
        if self.root is None:
            return []
        
        # Push the root node to the queue
        queue = [self.root]

        # List to store the BFS traversal results
        bfs = []

        # While there are nodes to process
        while queue:
            # Pop the first node from the queue
            node = queue.pop(0)

            # If the node is None (missing children), append None to the BFS list
            if node is None:
                bfs.append(None)
            
            # If the node is not None, append its key to the results and push its children to the queue
            else:
                bfs.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
        
        # Remove trailing None values
        while bfs and bfs[-1] is None:
            bfs.pop()
        
        # Return the BFS traversal list
        return bfs
    
    # Magic method: string representation of the tree
    # Support for the print() function
    def __str__(self):
        return pretty_tree(self)


    
    


    

    
            


