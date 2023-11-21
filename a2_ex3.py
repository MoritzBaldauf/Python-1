start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

even_counter = 0
odd_sum = 0

for i, val in enumerate(range(start, stop, step)):
    if i < 5:
        print(f"Number in iteration {i} = {val}")
    if val % 2 == 0:
        even_counter += 1
    else:
        odd_sum += val

print(f"Even number count = {even_counter}")
print(f"Sum of odd numbers = {odd_sum}")
