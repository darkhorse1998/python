def infiniteFib():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

fib = infiniteFib()
for _ in range(20):
    print(next(fib))