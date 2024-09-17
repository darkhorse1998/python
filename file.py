def fileWithOpen(fileName: str, fileContent: str, fileMode: str) -> None:
    file = open(fileName, fileMode)
    file.write(fileContent)
    file.close()

def fileWithWith(fileName: str, fileContent: str) -> None:
    with open(fileName, "w") as file:
        file.write(fileContent)

fileName1: str = "file1.txt"
fileName2: str = "file2.txt"
fileContent: str = "Hello World!!!\n"

fileWithOpen(fileName1,fileContent,"a")
fileWithWith(fileName2,fileContent)