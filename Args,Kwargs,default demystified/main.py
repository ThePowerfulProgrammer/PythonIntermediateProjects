

def sumArgs(*args):
    print(f"Args is a tuple: {args}")
    return sum(args)

def displayKwargs(**kwargs):
    print(f"Kwargs is a K:v (dict) {kwargs}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
    return ""

print(sumArgs(1,2,3,4,5,10,10))

print(displayKwargs(age=23,name='Ash', gender=1))
