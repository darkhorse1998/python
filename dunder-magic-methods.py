class Car:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        """
            This method basically decides the string representation of the class, i.e., 
            how the class should behave if someone tries to print it. Without this the 
            output will contain the class object and the memory reference.
        """
        return f"Car({self.name})"
    def __mul__(self, x) -> None:
        if type(x) is not int:
            raise Exception("Invalid Argument!")
        self.name = self.name * x 

car = Car("Honda")
print(car)
car * 5
print(car)

class fruit:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f"fruit({self.name})"
    def __call__(self, value):
        return value*100
    
d = fruit("Apple")
print(d)
print(d(10))