def round_(number, ndigits=None):

    # Round to 0 decimal places
    if ndigits is None:
        return "%0.0f" % number

    # Round to first , number
    elif ndigits == 0:
        if number % 1 >= 0.5:
            rem = number % 1
            number += 1 - rem
            return number

    # Round to ndigits
    else:
        string_number = str(number) # Convert to string to check length of comma part
        number_split = string_number.split(".")
        if len(number_split[1]) < ndigits: # Avoid printing of additional 0
            rounded_number = f"%0.{len(number_split[1])}f" % number
        else:
            rounded_number = f"%0.{ndigits}f" % number
        return rounded_number


#rounded_to_zero_decimal_places = round_(1777.7727, 3)
#print(rounded_to_zero_decimal_places)
