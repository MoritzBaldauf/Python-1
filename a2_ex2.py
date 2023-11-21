prev = curr = input("Enter number or 'x': ")

if curr == "x":
    print("Empty sequence")
else:
    while curr != "x" and int(prev) % 10 == int(curr) % 10:
        prev = curr
        curr = input("Enter number or 'x': ")
    
    if curr == "x":
        # First option to have left the while loop
        print("All numbers had the same digit in the ones place")
    else:
        # Second option to have left the while loop
        print(f"{prev} and {curr} differ in the ones place")
