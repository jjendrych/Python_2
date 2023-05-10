#zadanie 4.1
def add(a,b):
    return a+b
def od(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        print("operacja niemożliwa")
    else:
        return a/b

while True:
    choice=input("Wybierz działanie, które chcesz wykonać wpisując +, -, * lub /. Wpisz e aby zakończyć obliczenia:")
    if choice == "e":
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
