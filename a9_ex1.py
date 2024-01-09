
import re

def search_patterns(input_file, encoding = 'uft-8'):
    try:
        with open(f"{input_file}", 'r', encoding='utf-8') as file:
            content = file.read()

        while True:
            pattern = input("Enter pattern or press ENTER to exit: ")
            if not pattern:
                break

            matches = re.findall(pattern, content)
            print(f"{pattern}: {matches}")

    except FileNotFoundError:
        raise ValueError(f"'{input_file}' is not a file")

if __name__ == "__main__":
    try:
        file_name = input("Enter file name: ")
        search_encoding = input("Enter character encoding or press ENTER for default (utf-8): ") or 'utf-8'

        search_patterns(file_name, search_encoding)

    except Exception as e:
        print(f"Error: {e}")
