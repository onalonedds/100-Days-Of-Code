from multiprocessing import Manager, Pool


def worker(task, shared_list):
    # Workers can modify the shared list
    shared_list.append(f"Processed {task}")


if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list()  # Create a shared list
        tasks = range(5)  # Example tasks

        with Pool(processes=4) as pool:
            pool.starmap(worker, [(task, shared_list) for task in tasks])

        print(list(shared_list))
