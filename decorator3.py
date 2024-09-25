from datetime import datetime

def logger(func):
    def wrapper(*args):
        print(f"Function is called with arguments {args} at {datetime.now()}")
        return func(*args)
    return wrapper

logger(myFunc)()

@logger
def myFunc(msg: str) -> str:
    return msg

def printMsg(msg: str) -> None:
    print(f"Message is: {msg}")

if __name__ == "__main__":
    msgToFunc = "This is a message to be printed!"
    printMsg(myFunc(msgToFunc))