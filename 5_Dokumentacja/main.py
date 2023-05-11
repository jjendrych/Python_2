#zadanie 5
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
    

while True:
    choice=input("Wybierz działanie, które chcesz wykonać wpisując +, -, * lub /. Wpisz 0 aby zakończyć obliczenia:")
    if choice == "0":
        break
    
    if choice not in ["+","-","*","/"]:
        print("nie ma takiej operacji")
        continue
    
    a=float(input("Podaj pierwszą liczbę:"))
    b=float(input("Podaj drugą liczbę:"))
    if choice == "+":
        print("=",add(a,b)) 
    elif choice == "-":
        print("=",od(a,b))
    elif choice == "*":
        print("=",mul(a,b))
    elif choice == "/":
        print("=",div(a,b))
