
string = str(input("Enter comma-separated elements: "))
string_split = string.split(",")
string_dict = {}

i = 0
for i in range(len(string_split)):
    hex_value = 0
    if string_dict.get(string_split[i]) is not None:
        string_to_split = string_split[i]
        for j in range(len(string_to_split)):
            hex_value += ord(string_to_split[j])
        assert string_dict[string_split[i]] == hex_value
    else:
        string_to_split = string_split[i]  #This could be done with a function, but I am not sure if we are allowed to,
        # since it is only covered in the next lecture
        for j in range(len(string_to_split)):
            hex_value += ord(string_to_split[j])
        string_dict[string_split[i]] = hex_value

for keys, value in string_dict.items():
    print(f"'{keys}' -> {value}")
