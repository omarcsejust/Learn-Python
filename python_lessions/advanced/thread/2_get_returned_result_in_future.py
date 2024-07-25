import concurrent.futures
import time

'''
ThreadPool: Threads in the pool are executed concurrently and the control flow remains
in the pool until all threads are completed, no need to use th.join() method.
For example:

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_task, 3)
    f2 = executor.submit(do_task, 2)
    f3 = executor.submit(do_task, 3)
    
control comes here only when all threads in the ThreadPool are completed
'''


def do_task(sec):
    print("Starting Thread for {} sec".format(sec))
    time.sleep(sec)
    return sec


def get_result_sync():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_obj_1 = executor.submit(do_task, 3)
        r1 = future_obj_1.result()  # wait until the result of future_obj_1 is not found
        print(r1)

        future_obj_2 = executor.submit(do_task, 2)
        r2 = future_obj_2.result()  # wait until the result of future_obj_2 is not found
        print(r2)


def get_result_async():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_obj_1 = executor.submit(do_task, 3)
        future_obj_2 = executor.submit(do_task, 2)

        r1 = future_obj_1.result()  # wait until the result of future_obj_1 is not found
        print(r1)

        r2 = future_obj_2.result()  # wait until the result of future_obj_2 is not found
        print(r2)


def get_multiple_results_async():
    seconds = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # tasks = [executor.submit(do_task, sec) for sec in seconds]
        tasks = []
        for sec in seconds:
            future_obj = executor.submit(do_task, sec)
            tasks.append(future_obj)

        for task in tasks:
            print(task.result())


def get_result_as_completed():
    seconds = [5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # tasks = [executor.submit(do_task, sec) for sec in seconds]
        tasks = []
        for sec in seconds:
            future_obj = executor.submit(do_task, sec)
            tasks.append(future_obj)

        for future in concurrent.futures.as_completed(tasks):
            print(future.result())


def get_results_as_submitted_in_order():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        results = executor.map(do_task, seconds)

        for result in results:
            print(result)


start = time.perf_counter()

# get_result_sync()
# get_multiple_results_async()
# get_result_as_completed()
get_results_as_submitted_in_order()

end = time.perf_counter()

print(f"Total Time: {round(end - start)}")


