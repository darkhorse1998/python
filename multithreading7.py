from threading import Thread,Lock,current_thread
from time import sleep


def func1(myLock,msg) -> None:
    myLock.acquire()
    for _ in range(3):
        print(f"Current thread {current_thread().name} says {msg}")
    sleep(1)
    myLock.release()

myLock = Lock()
t1 = Thread(target=func1,args=(myLock,"Hello World!"))
t2 = Thread(target=func1,args=(myLock,"Message Delivered!"))
t3 = Thread(target=func1,args=(myLock,"Good Morning!"))

t1.start()
t2.start()
t3.start()