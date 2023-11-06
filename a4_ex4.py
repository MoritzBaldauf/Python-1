######## NOT DONE
def round_(number, ndigits=None):
    if ndigits is None:
        # Round to 0 decimal places, returning an integer
        return int(number + 0.5 if number > 0 else number - 0.5)
    else:
        # Round to ndigits precision, returning a float
        factor = 10 ** ndigits
        rounded_number = (number * factor + 0.5 if number > 0 else number * factor - 0.5)
        return rounded_number / factor



rounded_to_zero_decimal_places = round_(777.777, 0)
print(f"Rounded to 0 decimal places: {rounded_to_zero_decimal_places}")