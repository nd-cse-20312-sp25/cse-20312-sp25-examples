#!/usr/bin/env python3

from avl import AVLTree
import ast

def print_help():
    print("Commands:")
    print("  (q)uit")
    print("  (hel)p")
    print("  (cle)ar")
    print("  (ins)ert <value>")
    print("  (rem)ove <value>")
    print("  (wbf)s--write to BFS list")
    print("  (pri)nt")
    print()

def main():
    avl = AVLTree()
    print_help()

    while True:
        command_line = input("Enter command or (hel)p: ").strip().split()
        if not command_line:
            continue
        command = command_line[0].lower()
        
        # quit
        if command.startswith("q"):
            break
        # help
        elif command.startswith("hel"):
            print_help()
        # clear
        elif command.startswith("cle"):
            avl.clear()
            print("Cleared the avl.")
        # insert
        elif command.startswith("ins"):
            # Turn the rest of the command line into a single string
            arg_string = " ".join(command_line[1:])
            # Evaluate the string as a Python literal
            arg = ast.literal_eval(arg_string)
            avl.insert(arg)
            print(f"Inserted {arg} into the avl.")
            print(avl)
        # remove
        elif command.startswith("rem"):
            arg_string = " ".join(command_line[1:])
            arg = ast.literal_eval(arg_string)
            avl.remove(arg)
            print(f"Deleted {arg} from the avl.")
            print(avl)
        # write_bfs
        elif command.startswith("wbf"):
            print(avl.write_bfs())
        # print
        elif command.startswith("pri"):
            print(avl)
            
        else:
            print("Invalid command")
            print_help()

if __name__ == "__main__":
    main()