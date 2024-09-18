strings = ["egg", "apple", "elephant"]

valid_strings = [x
    for x in strings 
    if x[0].lower() == "a" or x[-1].lower() == "t"
    if x[0].lower() == "e"
]

print(valid_strings)

print("Flattened Matrix")

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [element for row in matrix for element in row]
print(flattened)

print("Categorize Odd & Even")

categorized = [
    "Even" if num % 2 == 0 else "Odd" for num in range(1,10)
]
print(categorized)

print("3D lists")

list3D = [[[x for x in range(5)] for _ in range(5)] for _ in range(5)]
print(list3D)

print("Create Dictionary")
listItem = [("a",1),("b",2),("c",3)]
dictItems = {k: v for k,v in listItem}
print(dictItems)
print(dict(listItem))

print("Set Comprehensions")
listItem = [1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5]
setItems = {x for x in listItem}
print(setItems)
