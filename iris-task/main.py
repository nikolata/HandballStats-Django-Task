from multithreading import ProducerThread, ConsumerThread
import time


if __name__ == '__main__':
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')
    print("Producer Thread is starting")
    p.start()
    time.sleep(2)
    print("Consumer Thread is starting")
    c.start()
    time.sleep(2)
