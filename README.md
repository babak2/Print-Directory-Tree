# Directory Tree Printer Script

This Python command-line program prints the underlying directory tree structure to the standard output (console/ terminal).


## Usage


- Ensure you have Python 3 installed on your system.

- Extract the contents of the zip file to a location on your computer.

- Open a terminal or command prompt.

- Navigate to the directory containing the print_dir_tree.py script.

- Run the script with the following command:

    - If Python 3 is the only Python version installed on your machine, you can use the python command. For example:

    `python print_dir_tree.py <directory_path> `

    - If both Python 2 and 3 are both installed, it's important to specify Python 3 using the python3 command. For example:

    `python3 print_dir_tree.py <directory_path> `


Replace <directory_path> with the path to the directory whose tree structure you want to print.

- The program will display the directory tree structure, showing directories suffixed by a trailing slash ('/') and files contained within each directory.     


### Example


Running the program with the command:


`python3 print_dir_tree.py path/`


will produce the following output:

path/
    subdir1/
        file1
        file2
    subdir2/
        file3
        subdir3/
            file4

