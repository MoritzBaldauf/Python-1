rows = int(input("Number of rows: "))  # i
cols = int(input("Number of cols: "))  # j

# Creating top of matrix
seq = [" ", ""]
for i in range(0, cols):
    seq.append(str(i))

print(*seq, sep=" ")
line = "  "
line += "--" * cols
print(line)

# Creating matrix filled with 0
Matrix = []
for i in range(0, rows):
    row = []
    for j in range(0, cols):
        if i == j:
            row.append("1")
        else:
            row.append("0")

    Matrix.append(row)

# printing
for i in range(0, rows):
    print(f"{i}|", end=" ")
    for j in range(0, cols):
        print(Matrix[i][j], end=" ")
    print()

