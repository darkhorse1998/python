import heapq

def keepMinFirst() -> heapq:
    arr = []
    print("Enter elements, q to stop\n")
    while True:
        ele = input()
        if (ele == "q"):
            break
        ele = int(ele)
        heapq.heappush(arr,ele)
    return arr

print(keepMinFirst())