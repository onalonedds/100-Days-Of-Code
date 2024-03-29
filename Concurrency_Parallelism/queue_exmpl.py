from multiprocessing import Queue, Process


def worker(task_queue, result_queue):
    while not task_queue.empty():
        task = task_queue.get()
        result_queue.put(task())


def task_1():
    print('Im singing!')
    return 'Im singing!'


def task_2():
    print('Im dancing!')
    return 'Im dancing!'


def task_3():
    print('Im playing piano!')
    return 'Im playing piano!'


if __name__ == "__main__":
    task_queue = Queue()
    result_queue = Queue()

    # Fill the task queue with tasks
    task_queue.put(task_1)
    task_queue.put(task_2)
    task_queue.put(task_3)

    processes = [Process(target=worker, args=(task_queue, result_queue)) for _ in range(3)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    # Collect all results
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print(results)
