#zadanie 3
import random
number=random.randrange(101)
"""liczba 101 się nie zawiera w randrange(), czyli mamy liczby 0-100"""

guess_num = 0 #inicjowanie sumy zgadnięć liczby przez użytkownika

while (True):
    print("Podaj swoją liczbę")
    num = int(input())
    if num==number:
        print("Brawo, zgadł*ś liczbę!")
        print("Próbował*ś zgadnąć liczbę ", guess_num, " razy!")
        print("Chcesz zagrać jeszcze raz? (wpisz tak lub nie)")
        odp=input()
        if odp in ["tak","Tak","T","t"]:
            continue
        else: 
            print("Dziękuje za grę!")
            break
    elif num > number:
            print("liczba jest mniejsza")
    else:
            print("Liczba jest większa")
    guess_num +=1