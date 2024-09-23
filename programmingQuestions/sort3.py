numList = [45,1,9,5,3,0,1]

numListLength = len(numList)

for i in range(numListLength):
    for j in range(i+1,numListLength):
        if(numList[i] > numList[j]):
            numList[i],numList[j] = numList[j],numList[i]

print(numList)