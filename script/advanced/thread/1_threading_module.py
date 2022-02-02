import threading
import time


def print_epoch(thread_name: str, delay: int):
    count = 0
    while count < 5:
        count += 1
        time.sleep(delay)
        print(thread_name, "-------------", time.time())


if __name__ == "__main__":
    t1 = threading.Thread(target=print_epoch, args=("thread-1", 1))
    t2 = threading.Thread(target=print_epoch, args=("thread-2", 2))

    t1.start()  # start thread t1
    t2.start()  # start thread t2

    t1.join()  # wait until thread t1 is finished
    t2.join()  # wait until thread t2 is finished


