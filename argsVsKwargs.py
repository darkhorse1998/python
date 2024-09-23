def func(a,b,c="default",d=False):
    print(a,b,c,d)

func(*[1,2], **{"c": "London", "d": True})

def func1(*args, **kwargs):
    print(args, kwargs)

func1(1,2,3,4,5,target="target",mission="complete")