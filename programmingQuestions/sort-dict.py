
dict1 = {
    "Lion": 999,
    "Tiger": 888,
    "Crocodile": 777
}

print(f"Sorted by keys: {sorted(dict1.items(),key=lambda x: x[0])}")
print(f"Sorted by values: {sorted(dict1.items(),key=lambda x: x[1])}")

dict2 = [
    {"name": "Lion", "power": 999},
    {"name": "Tiger", "power": 888},
    {"name": "crocodile", "power": 777}
]

print(f"Sorted by keys: {sorted(dict2,key=lambda x: x['name'])}")
print(f"Sorted by values: {sorted(dict2,key=lambda x: x['power'])}")