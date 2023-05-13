#zadanie 5.2
def add(a:float,b:float)->float:
    """Dodaje dwie liczby do siebie """
    return a+b
def od(a:float,b:float)->float:
    """Odejmuje drugą liczbę od pierwszej"""
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
    

while True:
    print()
    print("Menu kalkulatora:")
    print("1.Dodawanie")
    print("2.Odejmowanie")
    print("3.Mnożenie")
    print("4.Dzielenie")
    print("5.Wyjście z kalkulatora")
    choice=input("Wybierz działanie, które chcesz wykonać podając odpowiednią liczbę:")
    if choice == "5":
        break
    
    if choice not in ["1","2","3","4"]:
        print("nie ma takiej operacji")
        continue
    
    a=float(input("Podaj pierwszą liczbę:"))
    b=float(input("Podaj drugą liczbę:"))
    if choice == "1":
        print("=",add(a,b)) 
    elif choice == "2":
        print("=",sub(a,b))
    elif choice == "3":
        print("=",mul(a,b))
    elif choice == "4":
        print("=",div(a,b))
