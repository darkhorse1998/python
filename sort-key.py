print("SORT LIST")
elements: list[int] = [5,6,11,1,-1]
print(sorted(elements))

print("SORT DICTIONARY")
people = [
    {"name": "Ram", "age": 32},
    {"name": "Sam", "age": 16},
    {"name": "Jam", "age": 48},
    {"name": "Ham", "age": 99}
]
print(sorted(people,key=lambda person: person["age"]))
print(sorted(people,key=lambda person: person["age"],reverse=True))