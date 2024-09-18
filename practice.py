from typing import Any


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