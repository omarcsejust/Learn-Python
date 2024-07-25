from functools import lru_cache
import time


@lru_cache(maxsize=3)  # cache last 3 call
def some_time_consuming_work(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("Starting task call 1.......")
    some_time_consuming_work(4)
    print("End task call 1......")

    print("Starting task call 2.......")
    some_time_consuming_work(2)
    print("End task call 2......")

    print("Starting task call 3.......")
    some_time_consuming_work(4)  # same value passed again, so this call won't take time
    print("End task call 3......")



