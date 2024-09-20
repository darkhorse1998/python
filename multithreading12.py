from time import sleep,time
from threading import Thread

def callWebsite(url):
    print(f"requesting {url}")
    sleep(1)

if __name__ == "__main__":
    n_start_time = time()
    websites = [f"https://www.website-{x}.com" for x in range(10)]
    [callWebsite(website) for website in websites]
    n_end_time = time()
    print(f"Total time taken on sequential calls is {n_end_time-n_start_time:.3f}")

    t_start_time = time()
    threads = [Thread(target=callWebsite,args=(url,)) for url in websites]
    [thread.start() for thread in threads]
    t_end_time = time()
    print(f"total time taken through threads is {t_end_time-t_start_time:.3f}")