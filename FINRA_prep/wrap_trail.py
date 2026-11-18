
from time import time, sleep

def calc_time(func):

    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"{func.__name__} took {(end_time - start_time)} seconds")
        return result
    return inner


@calc_time
def Sleep_10():
    sleep(3)


Sleep_10()
