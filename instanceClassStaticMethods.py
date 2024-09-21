class demo():
    # class variable
    objectCount = 0
    
    def __init__(self,name) -> None:
        self.name = name
        self.increaseObjectCount()

    @classmethod
    def increaseObjectCount(cls) -> None:
        cls.objectCount+=1

    @classmethod
    def getObjectCount(cls) -> int:
        return cls.objectCount
    
    def getNameInUpperCase(self) -> str:
        return self.converToUpperCase(self.name)

    @staticmethod
    def converToUpperCase(name: str) -> str:
        return name.upper()
    
if __name__ == "__main__":
    d1 = demo("Ram")
    d2 = demo("Sam")
    d3 = demo("Tim")

    print(d1.getNameInUpperCase())
    print(d2.getNameInUpperCase())
    print(d3.getNameInUpperCase())

    print(demo.objectCount)