def navigationWithoutZip(nameList: list[str], ageList: list[int]) -> None:
    for index in range(min(len(nameList),len(ageList))):
        print(f"{nameList[index]} is {ageList[index]} years old")

def navigationWithZip(nameList: list[str], ageList: list[int]) -> None:
    combined = zip(nameList,ageList)
    for name, age in combined:
        print(f"{name} is {age} years old")

nameList: list[str] = ["Ram", "Sam", "Raghu", "Tim"]
ageList: list[int] = [23,45,21]

print("WITHOUT ZIP")
navigationWithoutZip(nameList,ageList)
print("WITH ZIP")
navigationWithZip(nameList,ageList)