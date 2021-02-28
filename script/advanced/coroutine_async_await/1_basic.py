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


if __name__ == "__main__":
    asyncio.run(main())





