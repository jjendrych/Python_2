#zadanie2
print("Podaj swoje słowo:")
word=input()
word_backwards=word[::-1]
if word==word_backwards:
    print("Słowo jest palindromem")
else:
    print("słowo nie jest palindoromem")