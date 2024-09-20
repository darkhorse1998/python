import time

# Decorator for capturing time taken to run functions
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        out = func(*args, **kwargs)
        total_time = time.time() - start
        print(f"Total time for function execution is {total_time:.5f}")
        return out
    return wrapper

@timer
def getBills(x):
    for i in range(x):
        c = 0
        c = c + i

getBills(1000000)