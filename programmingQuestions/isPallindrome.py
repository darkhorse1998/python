import string

punctuations = string.punctuation
digits = string.digits

def validator(func) -> bool:
    def wrapper(*args, **kwargs):
        if(len(args[0]) <= 2):
            print(f"{args[0]} is invalid!")
            return False
        
        if(args[0] in punctuations or args[0] in digits):
            print(f"{args[0]} contains digits! Invalid input!")
            return False
        
        out = func(*args, **kwargs)
        return out
    return wrapper

@validator
def isPallindrome(s):
    if (s == s[::-1]):
        print(f"{s} is a pallindrome")
    else:
        print(f"{s} is not a pallindrome")

if __name__ == "__main__":
    s = input("Enter the string: ")
    isPallindrome(s)