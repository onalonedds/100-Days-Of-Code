import multiprocessing
import time


def square(num):
    """Squares a number."""
    time.sleep(1)  # Simulate some work
    return num * num


def main():
    # Create a pool of processes
    pool = multiprocessing.Pool(processes=4)

    # Submit tasks to the pool
    results = pool.map(square, [1, 2, 3, 8])

    # Print the results
    print(results)

    # Close the pool
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
