def add(a:float,b:float)->float:
    return a+b
def od(a:float,b:float)->float:
    return a-b
def mul(a:float,b:float)->float:
    return a*b
def div(a:float,b:float)->float:
    if b == 0:
        print("operacja niemożliwa")
    else:
        return a/b