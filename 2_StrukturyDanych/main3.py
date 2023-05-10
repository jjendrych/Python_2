#zadanie3
mylist=["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
print("Podaj literę:")
letter=input()
for element in mylist:
    if element.startswith(letter):
        print(element)