
class A():
    def __init__(self) -> None:
        print("A")
        self.name = "A"
    def run(self):
        print("This is run() method for Class A")

class B(A):
    def __init__(self) -> None:
        print("B")
        self.name = "B"
        super().__init__()
    
    def run(self):
        print("This is run() method for Class B")

class C(A):
    def __init__(self) -> None:
        print("C")
        self.name = "C"
        super().__init__()

    def run(self):
        print("This is run() method for Class C")

class D(B,C):
    def __init__(self) -> None:
        super().__init__()
        self.name = "D"
        print("D")
        

d = D()
print(D.__mro__)

d.run()
print(d.name)