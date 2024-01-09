import argparse
import subprocess

def execute_program(program, args, timeout):
    try:
        command = [program] + args
        message = f"Running program '{program}' with arguments {args} with a {timeout}s timeout" if args else f"Running program '{program}' without any arguments with a {timeout}s timeout"
        print(message)

        completed_process = subprocess.run(command, timeout=timeout, text=True, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if completed_process.stderr:
            print(f"The '{program}' produced the following error output:\n{completed_process.stderr}")
        if completed_process.stdout:
            print(f"The '{program}' produced the following standard output:\n{completed_process.stdout}")
        print(f"The '{program}' finished with exit code {completed_process.returncode}")

    except FileNotFoundError:
        print(f"The specified program '{program}' could not be found")
    except subprocess.TimeoutExpired:
        print("The program execution timed out")

def main():
    parser = argparse.ArgumentParser(description="Execute a program with arguments and timeout")
    parser.add_argument("-p", "--program", type=str, required=True, help="Name of the program to be executed")
    parser.add_argument("-a", "--args", nargs='*', default=[], help="Arguments to be passed to the program")
    parser.add_argument("-t", "--timeout", type=float, default=60, help="Timeout in seconds for the execution of the program")

    args = parser.parse_args()

    execute_program(args.program, args.args, args.timeout)

if __name__ == "__main__":
    main()
