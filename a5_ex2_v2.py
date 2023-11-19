import os

def print_directory_recursively(dir_path, level):
    # List all files and subdirectories in the current directory
    contents = os.listdir(dir_path)

    # Iterate through each file or subdirectory
    for item in contents:
        # Create the full path to the item
        item_path = os.path.join(dir_path, item)

        # Indent based on the level
        indentation = '\t' * level

        # Check if the item is a directory
        if os.path.isdir(item_path):
            print(f"{indentation}{item}")
            # Recursively print the contents of the subdirectory
            print_directory_recursively(item_path, level + 1)
        # Check if the item is a file
        elif os.path.isfile(item_path):
            print(f"{indentation}{item}")
        else:
            # Invalid item (neither file nor directory)
            print(f"{indentation}{item} is invalid")

def print_directory(dir_path):
    # Check if dir_path is a valid path
    if os.path.exists(dir_path):
        # Check if dir_path is a file
        if os.path.isfile(dir_path):
            print(f"{dir_path} is a file not a directory")
        # Check if dir_path is a directory
        elif os.path.isdir(dir_path):
            print_directory_recursively(os.path.abspath(dir_path), 0)
    else:
        # Invalid path
        print(f"{dir_path} is invalid")

# Example usage:
print_directory("C:/Users/morit/Downloads/d0")
