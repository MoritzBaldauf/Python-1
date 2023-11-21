months = int(input("Please enter the duration of your subscription (in months): "))
price = None

if months <= 0:
    print("Invalid subscription duration")
elif months < 6:
    price = 6.5
elif months < 12:
    price = 5.9
else:
    # Integer-based solution
    postal_code = int(input("Please enter your postal code: "))
    
    if postal_code < 1000 or postal_code > 9999:
        print("Invalid postal code")
    else:
        middle = (postal_code // 10) % 100
        price = 4 + (middle / 100)
    
    # # String-based solution
    # postal_code = input("Please enter your postal code: ")
    #
    # if len(postal_code) != 4:
    #     print("Invalid postal code")
    # else:
    #     middle = int(postal_code[1] + postal_code[2])  # Or slicing: postal_code[1:3]
    #     price = 4 + (middle / 100)

if price is not None:
    print(f"The price per month is {price:.2f}")
    print(f"The full price for {months} months is {price * months:.2f}")
