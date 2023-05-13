def add(a,b):
    """Dodaje dwie liczby do siebie """
    return a+b
def od(a,b):
    """Odejmuje jedną liczbę od drugiej"""
    return a-b
def mul(a,b):
    """Mnoży jedną liczbę przez drugą"""
    return a*b
def div(a,b):
    if b == 0:
        print("operacja niemożliwa")
    else:
        return a/b