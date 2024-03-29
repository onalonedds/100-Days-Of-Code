import math
from multiprocessing import Pool, Lock, Value, Manager


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check_prime(num, queue):
    if is_prime(num):
        queue.put(num)


def main():
    numbers = range(10, 5000)  # The range of numbers to check

    # Using a Manager to create a list to store prime numbers (alternative to Queue)
    with Manager() as manager:
        prime_queue = manager.Queue()
        lock = Lock()
        prime_counter = Value('i', 0)

        # Using a Pool to distribute the task of checking for prime numbers
        with Pool(processes=10) as pool:
            [pool.apply_async(check_prime, args=(num, prime_queue)) for num in numbers]
            pool.close()  # No more tasks will be submitted
            pool.join()

        prime_list = manager.list()
        # Starting processes to update the shared counter whenever a prime is found
        while not prime_queue.empty():
            prime = prime_queue.get()
            prime_list.append(prime)
            with lock:
                prime_counter.value += 1

        # print(f"Prime numbers: {prime_list}")
        print(f"Total prime numbers found: {prime_counter.value}")


if __name__ == "__main__":
    main()
