"""Copy a file's contents from source to destination."""

# Add all of the required imports
import os
import shutil
import argparse
from pathlib import Path

# Define any functions used in your program
# Define a main function that reads in the contents of the source file
# and writes them to the destination file

def main():
    
    # Use argparse to grab all 4 arguments and make them of type path
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path1", type=Path)
    parser.add_argument("file_path2", type=Path)
    parser.add_argument("file_path3", type=Path)
    parser.add_argument("file_path4", type=Path)
    p = parser.parse_args()
    # Join 1+2 and 3+4 arguments to create complete paths
    path1 = os.path.join(p.file_path1, p.file_path2)
    path2 = os.path.join(p.file_path3, p.file_path4)
    # Print output message with path arguments
    print("\n")
    print("Source Path: ", path1)
    print("\n")
    print("Destination Path: ", path2)
    print("\n")
    # Check if the inputted paths exist
    if os.path.exists(path1) and os.path.exists(path2):
        # Copy contents from path1 into path2
        shutil.copy(path1, path2)
        print("Completed the copy from the source to the destination.")
        print("\n")
    # Print an error statement if the path does not exist
    else:
        print("Cannot copy due to incorrect source or destination path.")
        print("\n")


if __name__ == "__main__":
    main()