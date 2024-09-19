from threading import Thread,main_thread,active_count,enumerate

def countCalc(msg: str) -> None:
    print(msg)

t1 = Thread(target=countCalc,args=("Hello",))
t2 = Thread(target=countCalc,args=("World",))

print(f"Main thread is {main_thread}")
print(f"Current count of threads is {active_count()}")

print(f"Alive status of thread {t1.name} before starting is {t1.is_alive()}")
print(f"Alive status of thread {t2.name} before starting is {t2.is_alive()}")

t1.start()
print(f"Alive status of thread {t1.name} after starting is {t1.is_alive()}")
t2.start()
print(f"Alive status of thread {t2.name} after starting is {t2.is_alive()}")
print(f"Details of all running threads are \n{enumerate()}")