from tree_print import pretty_tree
import sys

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BSTree:
    # Constructor
    # Optionally, you can initialize the tree with a root node
    def __init__(self, root=None):
        self.root = root
    
    # Clear the tree
    def clear(self):
        pass

    # Insert a Node with a given key into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Helper function for insert
    def _insert(self, root, key):
        if root is None:
            pass
        if key == root.key:
            pass
        if key < root.key:
            pass
        else:
            pass
        return root

    # Magic method: check if the tree contains a key
    # Support for the 'in' operator
    def __contains__(self, key):
        return self._search(self.root, key)
    
    # Helper function for contains
    def _search(self, root, key):
        if root is None:
            pass
        if root.key == key:
            pass
        if key < root.key:
            pass
        pass  
    
    # Inorder traversal
    def inorder(self):
        return self._inorder(self.root)

    # Helper function for inorder
    def _inorder(self, root):
        if not root:
            return []
        pass

    # Magic method: et the length of the tree 
    # Support for the len() function 
    def __len__(self):
        return self._len(self.root)
    
    # Helper function for len
    def _len(self, root):
        if not root:
            return 0
        
        pass
    
    # Get the height of the tree
    def height(self):
        return self._height(self.root)
    
    # Helper function for height
    def _height(self, root):
        if root == None:
            pass
        pass

    # Remove a Node with a given key from the tree  
    def remove(self, key):
        self.root = self._remove(self.root, key)
    
    # Helper function for remove
    def _remove(self, root, key):
        if root is None:
            return root
        
        # Key is not yet found
        if key < root.key:
            pass
        elif key > root.key:
            pass

        # Key is found
        else:
            # Node with only one child or leaf node: return the non-null child
            # If the node has no children, return None
            if root.left is None:
                pass
            if root.right is None:
                pass
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            pass
            # Delete the inorder successor
            pass
        return root
    
    # Helper function to find the minimum value node in a tree
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            pass
        return current.key

    # Write the BFS traversal of the tree to a list
    def write_bfs(self):
        # If the tree is empty, return an empty list
        if self.root is None:
            pass
        
        # Push the root node to the queue
        pass

        # List to store the BFS traversal results
        pass

        # While there are nodes to process
        while queue:
            # Pop the first node from the queue
            pass

            # If the node is None (missing children), append None to the BFS list
            if node is None:
                pass
            
            # If the node is not None, append its key to the results and push its children to the queue
            else:
                pass
        
        # Remove trailing None values
        pass
        
        # Return the BFS traversal list
        return bfs
    
    # Magic method: string representation of the tree
    # Support for the print() function
    def __str__(self):
        return pretty_tree(self)

    
    


    

    
            


