lst = [3,13,52,1,54,58765,34,3,52,2]

lstMax = lst[0]
lstMin = lst[0]

for i in range(len(lst)):
    if(lst[i] > lstMax):
        lstMax = lst[i]
    if(lst[i] < lstMin):
        lstMin = lst[i]

print(f"Minimum value is {lstMin}")
print(f"Maximum value is {lstMax}")