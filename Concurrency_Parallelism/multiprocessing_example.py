import multiprocessing
import time


def square(num, delay):
    """Squares a number."""
    time.sleep(delay)  # Simulate some work
    print(num * num)


def main():
    # Create a process
    process1 = multiprocessing.Process(target=square, args=(5, 1))
    process2 = multiprocessing.Process(target=square, args=(6, 4))

    # Start the process
    process2.start()
    process1.start()

    # Wait for the process to finish
    #process1.join()
    #process2.join()

    # Get the result (if applicable)
    # result = process.exitcode  # For non-returning functions


if __name__ == '__main__':
    main()
