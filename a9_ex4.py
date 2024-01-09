import argparse
import subprocess

def run_program(command, args, timeout):
    try:
        if args:
            command_with_args = [command] + args
            print(f"Running program '{command}' with arguments {args} with a {timeout}s timeout")
            result = subprocess.run(command_with_args, timeout=timeout, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            print(f"Running program '{command}' without any arguments with a {timeout}s timeout")
            result = subprocess.run(command, timeout=timeout, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print(f"The '{command}' finished with exit code {result.returncode}")

        if result.stderr:
            print("The '{command}' produced the following error output:")
            print(result.stderr)

        if result.stdout:
            print("The '{command}' produced the following standard output:")
            print(result.stdout)

    except FileNotFoundError:
        print(f"The specified program '{command}' could not be found")

    except subprocess.TimeoutExpired:
        print("The program execution timed out")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute arbitrary programs with arguments.")
    parser.add_argument("-p", "--program", type=str, required=True, help="Name of the program to be executed.")
    parser.add_argument("-a", "--args", type=str, nargs="+", default=[], help="Arguments to be passed to the program.")
    parser.add_argument("-t", "--timeout", type=float, default=60, help="Timeout in seconds for the execution of the program.")
    args = parser.parse_args()

    run_program(args.program, args.args, args.timeout)
