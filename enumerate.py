def enumerateListItems(listItem: list[str]) -> None:
    for index, item in enumerate(listItem):
        print(f"{index+1}. {item}")

animals: list[str] = ["lion", "cat", "dog", "tiger"]
enumerateListItems(animals)