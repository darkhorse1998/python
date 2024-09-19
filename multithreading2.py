from threading import Thread, current_thread

def hello():
    for _ in range(5):
        print("hello")

def world():
    for _ in range(5):
        print("world")

t1 = Thread(target=hello)
t2 = Thread(target=world)

t1.start()
t2.start()