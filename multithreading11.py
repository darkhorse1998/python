import threading
from time import sleep

def customExcepthook(args):
    print(f"Exception Occured in {threading.current_thread().name}")
    print(args[1],sep="\n")

def funcWithException():
    print("Name"+10)
    sleep(1)

def func1():
    for _ in range(3):
        print("Hello world!")

threading.excepthook = customExcepthook
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=funcWithException)

t1.start()
t2.start()

# t1.join()
t2.join()

print("Welcome!")
