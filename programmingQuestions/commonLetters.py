def convertToSet(string: str) -> set:
    return set(string)

def removeSpace(setString: set) -> set:
    if(" " in setString):
        setString.remove(" ")
    return setString

def commonLetters() -> None:
    str1: str = input("Enter first string: ")
    str2: str = input("Enter second string: ")

    setString1 = convertToSet(str1)
    setString2 = convertToSet(str2)

    commonLetters = removeSpace(setString1 & setString2)
    print(f"Common letters are : {','.join(sorted(list(commonLetters)))}")
    print(len(list(commonLetters)))

if __name__ == "__main__":
    commonLetters()