import time

def recur_fib(n,cache):
    if n in cache:
        return cache[n]
    
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    
    cache[n] = recur_fib(n-1, cache) + recur_fib(n-2, cache)
    return cache[n]

if __name__ == "__main__":
    cache = {}
    start_time = time.time()
    print(recur_fib(100,cache))
    print(f"Total time taken: {time.time()-start_time:.5f}")