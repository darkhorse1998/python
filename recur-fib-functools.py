import functools
import time,sys

@functools.cache
def recur_fib(n):
    if(n < 2):
        return n
    return recur_fib(n-1) + recur_fib(n-2)

if __name__ == "__main__":
    start_time = time.time()
    print(recur_fib(100))
    print(f"Total time taken: {time.time()-start_time:.5f}")