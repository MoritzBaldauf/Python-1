import argparse
import multiprocessing
import math

def sum_of_fractions(start: int, end: int) -> float:
    """Compute the sum of 1/k from start to end."""
    return sum(1/k for k in range(start, end + 1))

def compute_gamma(n: int, p: int) -> float:
    """Compute the Euler-Mascheroni constant approximation using n terms and p processes."""
    with multiprocessing.Pool(p) as pool:
        # Calculate the range of terms for each process
        ranges = [(i * n // p + 1, (i + 1) * n // p) for i in range(p)]
        # Perform parallel computation of the fractions sum
        results = pool.starmap(sum_of_fractions, ranges)
    # Calculate the Euler-Mascheroni constant
    return -math.log(n) + sum(results)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Euler-Mascheroni Constant Approximation")
    parser.add_argument("-n", type=int, default=1000, help="Number of terms in the sum")
    parser.add_argument("-p", "--processes", type=int, default=1, help="Number of processes")
    args = parser.parse_args()

    # Compute the Euler-Mascheroni constant approximation
    gamma = compute_gamma(args.n, args.processes)
    print(f"Euler-Mascheroni constant approximation ({args.n} terms): {gamma:.9f}")


