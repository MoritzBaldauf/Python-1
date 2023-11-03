
def split_list(lst: list, num_sublists: int):
    size = len(lst) / num_sublists
    for i in range(len(lst)):
        list_split = lst[i:i, size]

split_list([1,2,3], 1)