import string

def cleanString(rawString: str) -> str:
    return ''.join([x for x in rawString if x not in list(string.punctuation)])

def frequencyWords(inputString: str) -> dict:
    rawStringList = cleanString(inputString)
    stringList = rawStringList.split()
    stringDict = {}
    for stringItem in stringList:
        if stringItem not in stringDict.keys():
            stringDict[stringItem] = 0
        stringDict[stringItem]+=1
    return stringDict


if __name__ == "__main__":
    inputString = "This is a random sentence, which is often regarded as random because it has been crafted at random."
    print(frequencyWords(inputString))
