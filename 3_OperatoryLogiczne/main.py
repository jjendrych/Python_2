#zadanie 3.1
print("Podaj swój wiek:")
age=int(input())
print("Posiadasz prawo jazdy kategorii A2? wpisz tak lub nie")
agree=input()
if agree == "tak":
    print("Ile lat je posiadasz?")
    num=int(input())
    
if age >=24 or (age>=20 and agree=='tak' and num >=2):
    print("Możesz przystąpić do egzaminu na prawo jazdy kat. A")
else:
    print("Nie możesz przystąpić do egzaminu")
