from multiprocessing import Process, Queue
import time


def producer(queue, n):
    """Producer function that generates numbers and puts them into the queue."""
    for i in range(n):
        print(f'Produced {i}')
        queue.put(i)  # Put the generated item into the queue
        time.sleep(1)  # Simulate time-consuming production
    queue.put(None)  # Signal to consumer that production is done


def consumer(queue):
    """Consumer function that processes items from the queue."""
    while True:
        item = queue.get()  # Retrieve an item from the queue
        if item is None:
            break  # Exit if the producer signals it is done
        print(f'Consumed {item}')
        time.sleep(2)  # Simulate time-consuming consumption


if __name__ == '__main__':
    queue = Queue()  # Create a shared queue for producer and consumer

    # Create the producer and consumer processes
    producer_process = Process(target=producer, args=(queue, 5))
    consumer_process = Process(target=consumer, args=(queue,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for both processes to complete
    producer_process.join()
    consumer_process.join()

    print("Production and consumption have completed.")
