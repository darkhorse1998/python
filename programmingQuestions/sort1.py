NUM_LIST = [5,9,1,3,6,11,27,12]

LENGTH_NUM_LIST = len(NUM_LIST)
SEQUENCE = [0]*(max(NUM_LIST)+1)
for num in NUM_LIST:
    SEQUENCE[num]+=1

c = 0
SORTED_LIST = []
for i in range(len(SEQUENCE)):
    if(c >= LENGTH_NUM_LIST):
        break
    if(SEQUENCE[i] != 0):
        SORTED_LIST.append(i)
print(SORTED_LIST)
SEQUENCE = None