import math as m
from math import sin

print(f"Value of sin(90 degrees) according to function sin imported from math module is {sin(m.pi/2)}")

def sin(x):
    return x*100

print(f"Value of sin(90 degrees) according to function we declared is {sin(m.pi/2)}")
print(f"Value of sin(90 degrees) according to function in math module is {m.sin(m.pi/2)}")