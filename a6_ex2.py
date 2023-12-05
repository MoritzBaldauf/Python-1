import os


def chunks(path: str, size: int, **kwargs):
    if not os.path.isfile(path): # Check if path is ok
        raise ValueError("The specified path is not a valid file.")

    if size < 1: # Chunks need to be >1 to be readable
        raise ValueError("Size must be greater than 0.")

    chunks_list = []

    # Open the file and read in chunks
    with open(path, **kwargs) as file: # kwargs passes arguments like mode to open function
        while True:
            data = file.read(size) # read byte data chunk of size
            if not data:
                break
            chunks_list.append(data) # add new chunk to list

    return chunks_list # return lst with elements size max 25, last element can be less than 25


#Testing
#if __name__ == "__main__":
#    for i, c in enumerate(chunks(f"{path}ex2_example.txt", 25, mode="rb")):
#        print(f"Chunk {i} = {c}")
