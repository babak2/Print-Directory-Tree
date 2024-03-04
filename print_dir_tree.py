"""
Print Directory Tree program 

This program prints the directory tree structure starting from the specified directory.

Usage:
    python3 print_dir_tree.py <directory_root>

Arguments:
    directory_root: The path to the directory to be printed.

Author: Babak Mahdavi Ardestani
Date: 1 March 2024

"""

import os
import sys


"""
print_directory_tree:
Recursive function that prints the directory tree structure starting from the specified directory on the console/ terminal.
It iterates through each directory and/or file in the specified directory, printing their names with appropriate indentation.
Parameters:
    directory (str): The path to the directory to be printed.
    indent (str): Optional. The current indentation string used for formatting.
"""
def print_directory_tree(directory, indent=''):

    if directory.endswith("/"):
        directory = directory[:-1]  # remove "/" character.

    print(indent + os.path.basename(directory) + "/")

    indent += "    "

    #for each file or directory item in the returned list of the names of file or directory items in the directory specified by the directory path 
    for item in os.listdir(directory): 
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print_directory_tree(item_path, indent)
        else:
            print(indent + "" + item)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 print_dir_tree.py <directory_root>")
        sys.exit(1)

    directory_root = sys.argv[1]

    # Start with no indentation
    print_directory_tree(directory_root)  
