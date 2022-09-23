import time
import datetime


def timer(function_name, with_date=False):
    def wrap(function):
        def inner(*args, **kwargs):
            if with_date:
                date = datetime.datetime.now()
                print(f"Today is: {date}")
            start = time.time()
            x = function(*args, **kwargs)
            end = time.time()
            print(f"{function_name} execution time {end - start} seconds.")
            return x
        return inner
    return wrap


@timer(function_name="Adding", with_date=True)
def add(a, b):
    time.sleep(1)
    return a + b


@timer(function_name="Multiplying")
def multiply(a, b):
    time.sleep(1)
    return a * b


print(add(2, 2333452))
print(multiply(24, 38))
