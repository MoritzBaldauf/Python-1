n = int(input("Enter number of lines: "))

if n < 3:
    print("Invalid number of lines")
else:
    for i in range(n):
        if i == 0 or i == n - 1:
            print("-" * n)
        else:
            print("|" + (" " * (n - 2)) + "|")
