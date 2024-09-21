from collections import deque
import random
import heapq

# dq = deque()

# dq.append(1)
# print(dq)
# dq.appendleft(0)
# print(dq)
# dq.append(5)
# print(dq)
# dq.append(6)
# print(dq)

# dq.pop()
# print(dq)
# dq.popleft()
# print(dq)

## Use deque to find minimum from a list of a numbers

numList = [random.randint(1,100) for _ in range(3)]

numQueue = deque()
MIN = numList[0]
for num in numList:
    if(num >= MIN):
        numQueue.append(num)
    else:
        numQueue.appendleft(num)
        MIN = num

print(f"Minimum value from queue is {numQueue[0]}")
print(f"Minimum value from list is {min(numList)}")

heapList = []
for num in numList:
    heapq.heappush(heapList,num)

print(f"Minimum vaue from heapq is {heapList[0]}")

list2heap = numList
heapq.heapify(list2heap)
print(f"Minimum value by converting list to heapq by heapify is {list2heap[0]}")