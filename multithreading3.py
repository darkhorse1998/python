from threading import Thread

class demo:
    def func1(self,name,type,extra):
        for _ in range(5):
            print(f"Hello World from class with name as {name} and type as {type} and extra as {extra}")

obj1 = demo()
t1 = Thread(target=obj1.func1, args=("Ram","Person","Person"))
t1.start()

for _ in range(5):
    print("Welcome from main!")