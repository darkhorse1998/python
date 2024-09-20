def inifinite_sequence():
    num = 0
    while True:
        yield num
        num+=1

# Prints series infinitely without memory issues
# for i in inifinite_sequence():
#     print(i)

# Equivalent notion for generators (Generator Coprehensions)

large_sequence = (i for i in range(10000000))
# for i in large_sequence:
#     print(i)