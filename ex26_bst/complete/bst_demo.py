#!/usr/bin/env python3

from bst import BSTree

def main():
    bst = BSTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    print(bst)
    print(f"len(bst):         {len(bst)}")
    print(f"bst.inorder():    {bst.inorder()}")
    print(f"bst.height():     {bst.height()}")
    print(f"bst.write_bfs():  {bst.write_bfs()}")

    bst.remove(3)
    print("After removing 3:")
    print(bst)
    print(f"5 in bst:         {5 in bst}")
    print(f"3 in bst:         {3 in bst}")
    print(f"len(bst):         {len(bst)}")
    print(f"bst.inorder():    {bst.inorder()}")
    print(f"bst.height():     {bst.height()}")
    print(f"bst.write_bfs():  {bst.write_bfs()}")
    bst.clear()
    print(bst)

if __name__ == "__main__":
    main()