import asyncio
from time import sleep, time


async def square(num: int):
    sleep(5)
    return num**2


async def get_squares():
    num_li = [5, 10, 15, 20]
    task_li = []
    for i in num_li:
        task_li.append(asyncio.create_task(square(i)))

    return await asyncio.gather(*task_li)


def get_squares2():
    num_li = [5, 10, 15, 20]
    task_li = []
    for i in num_li:
        task_li.append(square2(i))

    return task_li


def square2(num: int):
    sleep(5)
    return num**2


if __name__ == "__main__":
    #print(square(10))
    s_time = time()
    res = asyncio.run(get_squares())
    e_time = time()
    print(res)
    print("Time: ", e_time - s_time)

    s2_time = time()
    print(get_squares2())
    e2_time = time()
    print("Time: ", e2_time - s2_time)


