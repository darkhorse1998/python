import time
from threading import Thread

WEBSITEs = [f"Website-{x}" for x in range(10)]

def accessWebsite(website: str) -> None:
    print(f"Accessing website: {website}")
    time.sleep(0.1)

def accessNormally(websiteList: list) -> None:
    [accessWebsite(website) for website in WEBSITEs]

def accessByThreads(websiteList: list)-> None:
    threads = [Thread(target=accessWebsite, args=(website,)) for website in WEBSITEs]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

n_start_time = time.time()
accessNormally(WEBSITEs)
print(f"Total time taken for normal execution: {time.time()-n_start_time}")

t_start_time = time.time()
accessByThreads(WEBSITEs)
print(f"Total time taken for threads execution: {time.time()-t_start_time}")