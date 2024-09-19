from threading import Thread
import time

def calcSquare(num):
    print(f"{num} ^ 2 = {num**2}")
    time.sleep(0.2)

def runThread(x):
    t1 = Thread(target=calcSquare,args=(x,))
    t2 = Thread(target=calcSquare,args=(x,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    runThread(12)