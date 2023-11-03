integers = []
text = []
counts = {}
string = str(input("Enter comma-separated elements: "))
string_split = string.split(",")

for i in range(len(string_split)):
    if string_split[i].isdecimal():
        integers.append(int(string_split[i]))

        if counts.get(string_split[i]) is not None: # check if value exists in dict
            counts[string_split[i]] = counts[string_split[i]] + 1
        else:
            counts[string_split[i]] = 1

    else:
        text.append(string_split[i])

print(f"integers: {integers}")
print(f"counts: {counts}")
print(f"rest: {text}")


