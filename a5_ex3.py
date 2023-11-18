
def gen_fibonacci(upper_bound):
    # try:
    # Error handling
    if not isinstance(upper_bound, float) or isinstance(upper_bound, int):
        raise TypeError

    if upper_bound == 0:
        fib = 0
        return fib
    elif upper_bound == 1:
        fib = 1
        return fib
# except ValueError: