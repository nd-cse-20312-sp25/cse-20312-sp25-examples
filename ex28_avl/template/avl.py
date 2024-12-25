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
    def _get_height(self, root):
        pass

    # Helper function to get the balance factor of a node
    # Note: The balance factor of a null node is 0
    def _get_balance(self, root):
        pass
    
    # Helper functions to rotate left for AVL balancing
    def _left_rotate(self, z):
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
        # Do the rotation
        pass

        # Update the heights
        pass

        # Return the new root
        pass

    # Helper functions to rotate right for AVL balancing
    def _right_rotate(self, z):
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
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    # Helper function to rebalance the tree after insertion or removal
    def _rebalance(self, root, key):
        # root: root of the tree
        # key: key of the node that was inserted or removed
        balance = self._get_balance(root)

        # Case 1 - Left Left
        #     3 (root)
        #    /
        #   2
        #  /
        # 1 (key)
        if balance > 1 and key < root.left.key:
            print(f"Left Left at {root.key}")
            pass
        
        # Case 2 - Right Right
        # 1 (root)
        #  \
        #   2
        #    \
        #     3 (key)
        if balance < -1 and key > root.right.key:
            print(f"Right Right at {root.key}")
            pass
        
        # Case 3 - Left Right
        #   __3 (root)
        #  /
        # 1
        #  \
        #   2 (key)
        if balance > 1 and key > root.left.key:
            print(f"Left Right at {root.key}")
            pass
        
        # Case 4 - Right Left
        # 1__ (root)
        #    \
        #     3
        #    /
        #   2 (key)
        if balance < -1 and key < root.right.key:
            print(f"Right Left at {root.key}")
            pass

        return root

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

        # Update the height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Rebalance the tree
        return self._rebalance(root, key)
    
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

        # Update the height of the current node      
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # Rebalance the tree
        return self._rebalance(root, key)
    
    # Helper function to find the minimum value node in a tree
    def _min_value_node(self, root):
        current = root
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


    
    


    

    
            


