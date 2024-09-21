def fib(n):
    a,b = 0,1
    for _ in range(n):
        yield b
        a,b = b,a+b

fib_s = fib(20)

[print(x) for x in fib_s]