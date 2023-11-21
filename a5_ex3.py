
def gen_fibonacci(upper_bound):
    # try:
    # Error handling
    if not (isinstance(upper_bound, float) or isinstance(upper_bound, int)):
        raise TypeError("Upperbound is not a number")
    if upper_bound < 0:
        raise ValueError("Fibonacci sequence is only possible for positive Integers")
    upper_bound = int(upper_bound)

    if upper_bound == 0:
        fib = [0]
        return fib
    elif upper_bound == 1:
        fib = [0,1,1]
        return fib
    else:
        fib_sequence = [0,1]
        n = 1
        for n in range(2, upper_bound+2):
            if (fib_sequence[n-1] + fib_sequence[n-2]) <= upper_bound:
                fib_sequence.append(fib_sequence[n-1] + fib_sequence[n-2])
            else:
                return fib_sequence
    return fib_sequence
