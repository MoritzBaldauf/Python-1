
import os

path = "C:/Users/morit/Downloads/d0"
def print_directory_recursively(dir_path: str):
    if os.path.isfile(dir_path):
        print("dir_path is a file not a directory")
    if os.path.isdir(dir_path):

        print(os.path.basename(dir_path))

        print(os.listdir(dir_path))
        print_directory_recursively(dir_path)
    else:
        print("dir_path is invalid")

print_directory_recursively(path)

