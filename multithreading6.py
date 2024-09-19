from threading import Thread,current_thread
import time

def func1() -> None:
    time.sleep(5)
    print(f"This output is from the {current_thread().name} thread and marks the completion of the function execution.")


if __name__ == "__main__":
    t1 = Thread(target=func1)
    t1.start()
    t1.join(timeout=2)
    print(f"Thread t1 is still alive after timeout of 2 seconds? {t1.is_alive()}")
    print(f"This output is from the {current_thread().name} thread")