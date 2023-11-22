import os


def print_directory(dir_path):  # main function
    if os.path.exists(dir_path):
        if os.path.isfile(dir_path):  # Check if file
            print(f"{dir_path} is a file not a directory")

        elif os.path.isdir(dir_path):  # Check if directory
            print_directory_recursively(os.path.abspath(dir_path), 0)
    else:
        print(f"{dir_path} is invalid")


def print_directory_recursively(dir_path, level):  # function to call recurisvly

    contents = os.listdir(dir_path)  # List all files and subdirectories in the current directory

    for item in contents:  # Iterate through each file or subdirectory
        item_path = os.path.join(dir_path, item)  # Create the full path to the item

        # Indent based on the level
        indentation = '\t' * level

        if os.path.isdir(item_path):  # Check if the item is a directory
            print(f"{indentation}{item}")
            print_directory_recursively(item_path, level + 1)  # Recursively print the contents of the subdirectory
        elif os.path.isfile(item_path):
            print(f"{indentation}{item}")  # Check if the item is a file
        else:
            print(f"{indentation}{item} is nether a file nor a directory")  # Invalid item (neither file nor directory)
