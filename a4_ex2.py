
def clip(*values, min_=0, max_=1):
    final_list = []
    for i in range(len(values)):
        if values[i] <= min_:
            final_list.append(min_)
        elif values[i] >= max_:
            final_list.append(max_)
        else:
            final_list.append(values[i])
    return final_list
