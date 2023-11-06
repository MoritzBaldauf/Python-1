

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
split_list([0,1,2,3,4,5,6,7], 3)