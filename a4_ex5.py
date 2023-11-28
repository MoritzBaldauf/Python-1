
def sort(elements: list, ascending: bool = True):
    i = 1
    for i in range(1, len(list)):
        current_list = elements[i]
        j = i - 1
        while j >= 0:
            if ascending:
                check_up_down = current_list < elements[j] # Check if prev element is bigger than current (Ascending)
            else:
                check_up_down = current_list > elements[j] # Other way around

            if check_up_down: # True when number hast to be changed
                elements[j + 1] = elements[j]
                j -= 1
            else:
                break
        elements[j + 1] = current_list # make sure current value is not lost because of replacement

#list = [1, 3, 0, 4, 5]
#sort(list, False)
#print(list)
