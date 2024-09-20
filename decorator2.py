
# Decorator for validating inputs of function
def validator(func):
    def wrapper(*args, **kwargs):
        if(args[0] > 10000):
            raise Exception("Input Exceeded!")
        else:
            out = func(*args, **kwargs)
            return out
    return wrapper

@validator
def func(x):
    for i in range(x):
        c = 0
        c = c + i
    print(f"Function func has been executed with c = {c}")

func(100)
func(1000000)