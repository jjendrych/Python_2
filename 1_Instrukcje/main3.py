#zadanie 3
import random
number=random.randrange(101)
print("Podaj swoją liczbę")
num = int(input())
while (True):
    if num==number:
        print("Brawo, zgadł*ś liczbę!")
        print("Chcesz zagrać jeszcze raz?")
        odp=input()
        if odp=="tak":
            continue
        else: 
            print("Dziękuje za grę!")
            break
    else:
        if num > number:
            print("liczba jest mniejsza")
        else:
            print("Liczba jest większa")