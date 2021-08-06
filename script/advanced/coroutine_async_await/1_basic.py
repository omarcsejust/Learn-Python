import asyncio
import time


async def print_time():
    start_time = time.time()

    while True:
        dur = int(time.time() - start_time)

        if dur%3 == 0:
            print("{} seconds have passed.".format(dur))
        await asyncio.sleep(1)


async def print_number():
    number = 1
    while True:
        print(number)
        number += 1
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_time())
    task2 = asyncio.create_task(print_number())

    await asyncio.gather(task1, task2)


async def test_001():
    print("Hello from test 001")
    await asyncio.sleep(5)
    print("Hello from test 001 after 5 sec")


async def test_002():
    print("Hello from test 002")


def test_003():
    print("Hello from test 003")
    asyncio.run(test_001())
    print("After")


async def main_test():
    test_task_001 = asyncio.create_task(test_001())
    test_task_002 = asyncio.create_task(test_002())
    await asyncio.gather(test_task_001, test_task_002)

if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(main_test())
    test_003()
    # asyncio.run(test_001())





