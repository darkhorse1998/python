def pyramid() -> None:
    symbol = "*"
    height = 10
    symbol_first_row = 1
    symbol_increament = 2
    last_row_length = symbol_first_row + ((height-1)*symbol_increament)

    for _ in range(0,height):
        print(f"{symbol*symbol_first_row:^{last_row_length}}")
        symbol_first_row+=symbol_increament

def invertedPyramid() -> None:
    symbol = "*"
    height = 10
    symbol_decreament = 2
    symbol_first_row = 1 + (height-1)*symbol_decreament
    symbol_count = symbol_first_row
    
    for _ in range(0,height):
        print(f"{symbol*symbol_count:^{symbol_first_row}}")
        symbol_count-=symbol_decreament

if __name__ == "__main__":
    while(True):
        choice = input(f"Enter choice in numbers:\n{'1.':5} Pyramid\n{'2.':5} Inverted Pyramid\n")
        if choice == "1":
            pyramid()
        elif choice == "2":
            invertedPyramid()
        elif choice.lower() == "q":
            break
        else:
            print("Incorrect choice! Try again!\n")
