import math
import sys

def sum_of_fractions(start, end):
    result = sum(1/k for k in range(start, end + 1))
    return result

def main():
    if len(sys.argv) == 1:
        print("Usage: python script.py -n <number_of_terms> -p <number_of_processes>")
        sys.exit(1)

    args = {"-n": 1000, "-p": 1}
    i = 1

    while i < len(sys.argv):
        if sys.argv[i] in args:
            args[sys.argv[i]] = int(sys.argv[i + 1])
            i += 2
        else:
            print(f"Invalid option: {sys.argv[i]}")
            sys.exit(1)

    terms_per_process = args["-n"] // args["-p"]

    ranges = [(i * terms_per_process + 1, (i + 1) * terms_per_process) for i in range(args["-p"])]

    results = [sum_of_fractions(start, end) for start, end in ranges]

    total_sum = sum(results)
    gamma_approximation = -math.log(args["-n"]) + total_sum

    print(f"Euler-Mascheroni constant approximation ({args['-n']} terms): {gamma_approximation:.9f}")

if __name__ == "__main__":
    main()
