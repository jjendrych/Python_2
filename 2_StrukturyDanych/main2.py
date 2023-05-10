#zadanie2
print("Podaj swoje słowo:")
word=input()
drow=word[::-1]
if word==drow:
    print("Słowo jest palindromem")
else:
    print("słowo nie jest palindoromem")