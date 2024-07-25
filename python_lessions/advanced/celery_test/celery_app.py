from celery import Celery

REDIS_BASE_URL = 'redis://localhost:6379'

app = Celery(
    'tasks',
    broker=f"{REDIS_BASE_URL}/0",
    backend=f"{REDIS_BASE_URL}/1"
)


@app.task
def say_hello():
    import time
    print("hello")
    time.sleep(10)
    print("End.......")


if __name__ == "__main__":
    say_hello.delay()



