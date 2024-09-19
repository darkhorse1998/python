from threading import Thread, current_thread

def func1(msg: str) -> None:
    count = 1
    for x in range(1000000):
        count+=1
    print(f"Thread ({current_thread().name}): Count value is = {count} and message is {msg}")

t1 = Thread(target=func1, args=("Hello!",))
t1.start()

print(f"Thread ({current_thread().name}): This ran outside the thread configured.")