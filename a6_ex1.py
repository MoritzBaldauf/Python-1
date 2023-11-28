
def file_statistics(path:str):
    lines = 0
    with open(f"{path}", "r") as rf:
        data = rf.read()

        line_split = data.split("\n")
        line_count = len(line_split)
        print(f"Lines {line_count}")

        # Counting words
        words = list(data.split())
        words_count = len(words)
        print(f"Words {words_count}")

        character_count = len(data)
        print(f"characters {character_count}")
        return


path = "C:/Users/morit/Downloads/Examples"
file_statistics(f"{path}/ex1_2.txt")

