import asyncio


class ParallerExecution:

    async def calculate_factorial(self, number):
        if number == 0:
            return 1
        return await self.calculate_factorial(number - 1) * number

    def execute_multiple_task_with_event_loop(self):
        nums = [5, 10, 15, 20]
        tasks = []
        for num in nums:
            tasks.append(self.calculate_factorial(num))
            # tasks.append(asyncio.create_task(self.calculate_factorial(num)))

        gather_tasks = asyncio.gather(*tasks)
        loop = asyncio.get_event_loop()
        fact_result = loop.run_until_complete(gather_tasks)
        loop.close()
        print(fact_result)

    async def execute_multiple_task_without_event_loop(self):
        tasks = []
        nums = [5, 10, 20, 30]
        for num in nums:
            tasks.append(self.calculate_factorial(num))
            # tasks.append(asyncio.create_task(self.calculate_factorial(num)))  # also working

        return await asyncio.gather(*tasks)

    def get_without_event_loop_result(self):
        result = asyncio.run(self.execute_multiple_task_without_event_loop())
        print(result)
        print(type(result))


if __name__ == '__main__':
    paraller_obj = ParallerExecution()
    paraller_obj.execute_multiple_task_with_event_loop()
    paraller_obj.get_without_event_loop_result()



