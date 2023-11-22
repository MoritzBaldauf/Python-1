def sub_summarize(nested: list, sub_sums: list):
    total = 0
    for number in nested: # iterating through loop
        if isinstance(number, list): # when numer is a list
            sublist_sum = sub_summarize(number, sub_sums) # recursive call the function
            total += sublist_sum # Func returns sum of sublist, add resulting sum to total
            sub_sums.append(sublist_sum) # Append sublist sum to sub_sum list
        else:
            total += number # base case
    return total
