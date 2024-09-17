print("FILTER FUNCTION...")
def validString(element: str) -> bool:
    return len(element) > 5
elements = ["my", "typical", "day", "is", "awesome"]
print(list(filter(validString, elements)))

print("LAMBDA FUNCTION...")
elements = ["my", "typical", "day", "is", "awesome"]
print(list(filter(lambda x: len(x) > 5, elements)))