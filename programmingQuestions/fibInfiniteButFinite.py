def infiniteFib():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

fib = infiniteFib()
for _ in range(20):
    print(next(fib))

# start_index = 10
# end_index = 20

# for i in range(end_index+1):
#     req_fib = next(fib)
#     if(i >= start_index and i <= end_index):
#         print(req_fib)