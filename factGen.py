def factGen(n):
    current = 1
    for i in range(1,n+1):
        current*=i
        yield current

fact = factGen(10)
for i in fact:
    print(i)