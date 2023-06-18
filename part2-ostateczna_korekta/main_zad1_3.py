#zadanie 3 - ostateczne korekty
import random
number=random.randrange(101)
"""liczba 101 się nie zawiera w randrange(), czyli mamy liczby 0-100"""

guess_num = 0 #inicjowanie sumy zgadnięć liczby przez użytkownika

while (True):
    print("Podaj swoją liczbę")
    num = int(input())
    guess_num +=1 #przeniesienie guess_num tutaj pozwoli na dodawanie strzału po każdej wpisanej przez użytkonika liczbie przez co weźmie  pod uwagę zwycięski strzał
    if num==number:
        print("Brawo, zgadł*ś liczbę!")
        print("Próbował*ś zgadnąć liczbę ", guess_num, " razy!") 
        print("Chcesz zagrać jeszcze raz? (wpisz tak lub nie)")
        odp=input()
        if odp in ["tak","Tak","T","t"]:
            guess_num=0 #przy wybraniu kontunuowaniu gry liczba strzałów jest tutaj resetowana -> ustawiana na 0
            continue
        else: 
            print("Dziękuje za grę!")
            break
    elif num > number:
            print("liczba jest mniejsza")
    else:
            print("Liczba jest większa")
    