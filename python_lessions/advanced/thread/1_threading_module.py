import threading
import time


def print_epoch(thread_name: str, delay: int):
    count = 0
    while count < 5:
        count += 1
        time.sleep(delay)
        print(thread_name, "-------------", time.time())


def do_task(thread_no, delay_sec):
    print("Starting Thread {}".format(thread_no))
    time.sleep(delay_sec)
    print("Ending Thread {}".format(thread_no))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_epoch, args=("thread-1", 1))
    t2 = threading.Thread(target=print_epoch, args=("thread-2", 2))

    t1.start()  # start thread t1
    t2.start()  # start thread t2

    t1.join()  # wait until thread t1 is finished
    t2.join()  # wait until thread t2 is finished

    # do_task method
    start = time.perf_counter()

    t3 = threading.Thread(target=do_task, args=[1, 3])
    t4 = threading.Thread(target=do_task, args=[2, 2])

    t3.start()
    t4.start()

    # MAIN PROGRAM WILL BE EXITED
    # t3.join()
    # t4.join()

    end = time.perf_counter()

    print("Time taken {}".format(round(end - start)))


