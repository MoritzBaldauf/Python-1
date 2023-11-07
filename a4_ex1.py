


def split_list(lst, num_sublists):
    if num_sublists == 0:
        return lst

    #if num_sublists >= len(lst):
     #   return [[x] for x in lst]

    avg_size = round(len(lst) / num_sublists)
    remainder = len(lst) % num_sublists
    sublists = []

    start = 0
    for i in range(num_sublists):
        count_itter = 0
        if i < remainder:
            sublist_size = avg_size + 1
        else:
            sublist_size = avg_size
            sublists.append(lst[start:start + sublist_size:i+num_sublists])
            #sublists.append(lst)
            while count_itter <= len(lst):
                sublists[i].extend(lst[start:len(lst):i+num_sublists])
                count_itter += 1
        start += 1

    return sublists

# Example usage:
original_list = [0,1,2,3]
num_sublists = 2
result = split_list(original_list, num_sublists)
print(result)


## OLD VERSION
'''
def split_list(lst: list, num_sublists: int):
    size_counter = 0

    list_split = []
    first = []
    end = []
    final_list = []
    size = round(len(lst) / num_sublists)
    remainder = len(lst) % num_sublists

    for i in range(len(lst)):
        for size_counter in range(1,size+1):
            if i % size_counter == 0:
                first.append(lst[i])
            elif i % size_counter == 0:
                list_split.append(lst[i])
            else:
                end.append(lst[i])

        #if size_counter < size:
         #   size_counter += 1
        #else:
         #   size_counter = 0
    final_list.append(first)
    final_list.append(list_split)
    final_list.append(end)

    print(final_list)
split_list([0,1,2,3,4,5,6,7], 3) '''