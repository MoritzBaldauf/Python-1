# Change this code a bit
def sort(elements: list, ascending: bool = True):
    i = 1
    for i in range(1, len(list)):
        current_list = elements[i]
        j = i - 1
        while j >= 0 and ((current_list < elements[j]) if ascending else (current_list > elements[j])):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = current_list


list = [1, 3, 0, 4, 5]
sort(list, False)
print(list)
