def split_list(lst: list, num_sublists: int) -> list:
    sublist = []

    if num_sublists == 0:
        return [lst]

    for i in range(num_sublists):  # Create empty list
        sublist.append([])

    # Filling list
    index = 0
    for value in lst:
        sublist[index].append(value)
        index += 1
        if index == num_sublists:
            index = 0
    return sublist
