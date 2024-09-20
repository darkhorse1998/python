import sys

INPUT = 1000000
x = [x**2 for x in range(INPUT)]
print(f"Size of normal output = {sys.getsizeof(x)}")
x = None

def gen(n):
    for i in range(n):
        yield i ** 2

g = gen(INPUT)
print(f"Size of generator output = {sys.getsizeof(g)}")

SUM = 0
for i in g:
    SUM+=i
print(SUM)

SUM, g, i = None, None, None