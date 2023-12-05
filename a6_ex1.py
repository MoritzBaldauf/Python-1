import os

def file_statistics(path: str):
    if not path.endswith('.txt'):  # check if textfile
        raise ValueError(f"Path {path} is not a text file")

    # counters
    line_count = 0
    word_count = 0
    char_count = 0
    digit_count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:  # open file in read & UTF-8
            for line in file:  # run through each line of file
                line_count += 1
                words = line.split()  # split by space, save in list
                word_count += len(words)
                char_count += len(line.replace('\r', ''))  # Dont include carriage returns (\r) in char count

                for char in line: # go through each char of the line str
                    if char.isdigit(): # check if digit
                        digit_count += 1

        print('--------------------')
        print(f"Statistics of file {os.path.basename(path)}:")
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
        print(f"Number of digits: {digit_count}")
        print('--------------------')

    except FileNotFoundError: # Error if not a path
        raise OSError(f"Path {path} does not exist")
