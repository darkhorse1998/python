
def infSequence():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

fib = infSequence()
# n = 10
# for _ in range(n):
#     print(next(fib))

reqd_fib_position = 100
for i in range(reqd_fib_position):
    fib_req = next(fib)
    if(i == reqd_fib_position-1):
        print(f"Required {reqd_fib_position} fibonacci number is {fib_req}")