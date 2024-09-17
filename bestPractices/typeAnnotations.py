def convert_to_uppercase(itemList: list[str]) -> list[str]:
    """
    This function takes in a list of strings and returns the list with all of its elements in uppercase
    """
    return [x.upper() for x in itemList]

def convert_each_letter_to_uppercase(itemList: list[str]) -> list[str]:
    """
    This function takes in a list of strings and returns the list with all of its elements in uppercase
    """
    newItemList = map(convert_to_uppercase, itemList)
    return list(newItemList)

if __name__ == "__main__":
    elements = ["apple", "ball", "cat"]
    print(convert_to_uppercase(elements))
    print(convert_each_letter_to_uppercase(elements))
    print(convert_to_uppercase.__doc__)