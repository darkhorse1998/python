# import time
# from threading import Thread

# WEBSITEs = [f"Website-{x}" for x in range(10)]

# def accessWebsite(website: str) -> None:
#     print(f"Accessing website: {website}")
#     time.sleep(0.1)

# def accessNormally(websiteList: list) -> None:
#     [accessWebsite(website) for website in websiteList]

# def accessByThreads(websiteList: list)-> None:
#     threads = [Thread(target=accessWebsite, args=(website,)) for website in websiteList]
#     [thread.start() for thread in threads]
#     [thread.join() for thread in threads]

# n_start_time = time.time()
# accessNormally(WEBSITEs)
# print(f"Total time taken for normal execution: {time.time()-n_start_time}")

# t_start_time = time.time()
# accessByThreads(WEBSITEs)
# print(f"Total time taken for threads execution: {time.time()-t_start_time}")

# str1 = "my demo call is today at IST hours which is supposed to be a demo call wth me in the demo"

# dict1 = {}
# def findMostFrequentWord(str1: str):
#     dict1 = {}
#     for i in str1.split():
#         if(i not in dict1.keys()):
#             dict1[i] = 0
#         dict1[i] +=1
    
#     print(max(dict1.items(), key=lambda x: x[1]))

# findMostFrequentWord(str1)


# def recurFib(n, dict1):
#     if(n in dict1.keys()):
#         return dict1[n]
#     if(n <= 1):
#         return n
#     dict1[n] = recurFib(n-1, dict1) + recurFib(n-2, dict1)
#     return dict1[n]

# dict1 = {}
# print(recurFib(100, dict1))

# def factGen(n):
#     current = 1
#     for i in range(1,n+1):
#         current *= i
#         yield current

# fact = factGen(10)
# for i in fact:
#     print(i)

def rec_fib(n, cache):
    if(n in cache.keys()):
        return cache[n]
    if(n <= 1):
        return n
    cache[n] = rec_fib(n-1, cache) + rec_fib(n-2, cache)
    return cache[n]

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    cache = {}
    for i in range(1,n+1):
        print(rec_fib(i, cache))