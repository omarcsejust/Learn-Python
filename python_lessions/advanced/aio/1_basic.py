import asyncio


async def task(text: str, delay: int):
    print("Starting......{}".format(delay))
    await asyncio.sleep(delay)
    print(text)


# main and main2 are same, i.e: both are synchronous
async def main():
    await task("Finished 1......", 1)
    await task('Finished 2........', 2)


async def main2():
    task1 = asyncio.create_task(task("Finished 1......", 1))
    await task1

    task2 = asyncio.create_task(task('Finished 2......', 2))
    await task2


async def main3():
    task1 = asyncio.create_task(task("Finished.......3", 3))
    task1 = asyncio.create_task(task("Finished.......2", 2))
    print("Exit from main thread......")


async def main4():
    task1 = asyncio.create_task(task("Finished 3......", 3))
    task2 = asyncio.create_task(task('Finished 2......', 2))

    await task1
    await task2


asyncio.run(main3())


