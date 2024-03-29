import threading
import multiprocessing
import time


def task(name):
    print(f"Task {name}: Starting")
    time.sleep(2)  # Simulate some work
    print(f"Task {name}: Finishing at {time.time()}")


if __name__ == '__main__':
    # Using threads
    for i in range(3):
        thread = threading.Thread(target=task, args=(i,))
        thread.start()  # Start the threads but don't wait for them
        thread.join()

    print("Main program: All threads started")

    # Using processes

    pool = multiprocessing.Pool(processes=3)
    results = pool.map(task, [1, 2, 3])
    pool.close()
    pool.join()

    print("Main program: All processes started")
