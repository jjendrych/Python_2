def add(a:float,b:float)->float:
    """Dodaje liczbę pierwszą do drugiej"""
    return a+b
def od(a:float,b:float)->float:
    """Odejmuje drugą liczbe od drugiej"""
    return a-b
def mul(a:float,b:float)->float:
    """Mnoży pierwszą liczbę przez drugą"""
    return a*b
def div(a:float,b:float)->float:
    """Dzieli pierwszą liczbę przez drugą"""
    if b == 0:
        print("operacja niemożliwa")
    else:
        return a/b