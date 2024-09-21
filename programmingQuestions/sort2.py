from itertools import repeat

NUM_LIST = [5,9,1,3,6,11,27,12,1,2,3,1,2,1,21,2,1,2,1,1,2,1,2,1,1]

LENGTH_NUM_LIST = len(NUM_LIST)
SEQUENCE = [0]*1000
for num in NUM_LIST:
    SEQUENCE[num]+=1

c = 0
SORTED_LIST = []
for i in range(len(SEQUENCE)):
    if(c >= LENGTH_NUM_LIST):
        break
    if(SEQUENCE[i] != 0):
        SORTED_LIST.extend(repeat(i,SEQUENCE[i]))
        c+=SEQUENCE[i]
print(SORTED_LIST)
SEQUENCE = None