from threading import Thread

def getEvenNumbers(numList, resultList):
    [resultList.append(x) for x in numList if x % 2 == 0]

resultList = []
numList = list(range(1,51))

t1 = Thread(target=getEvenNumbers, args=(numList,resultList))
t1.start()

print(resultList)