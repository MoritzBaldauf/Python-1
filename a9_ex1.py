
import re
import os

def search_patterns_in_file():
    input_file = input("Enter file name: ")
    if not os.path.isfile(input_file):
        raise ValueError(f"'{input_file}' is not a file")

    encoding = input("Enter character encoding or press ENTER for default (utf-8): ")
    if not encoding:
        encoding = 'utf-8'

    while True:
        pattern = input("Enter pattern or press ENTER to exit: ")
        if not pattern:
            break

        try:
            compiled_pattern = re.compile(pattern)
        except re.error:
            print(f"Invalid regular expression pattern: {pattern}")
            continue

        with open(input_file, 'r', encoding=encoding) as file:
            file_content = file.read()
            matches = compiled_pattern.findall(file_content)
            print(f"{pattern}: {matches}")

search_patterns_in_file()
