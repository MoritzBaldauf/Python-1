i = 0
string = []
while True:
    string.append(input("Enter element or 'x' when done: "))

    if string[i] == "x" and i == 0:
        print(f"all: {[]}")
        print(f"unique (sorted): {[]}")
        break
    elif string[i] == "x" and i > 0:
        string = string[:i]
        print(f"all: {string}")
        list_sorted = sorted(string)
        list_sorted = list(dict.fromkeys(list_sorted))
        # creating dict with list values as keys -> dict cant have a double key
        print(f"unique (sorted): {list_sorted}")
        break
    i += 1
