from os import path
with open('tekst.txt','r') as note:
    a=note.read()
    SumaWyrazow = len(a.split())
    print("suma wyrazów wynosi",SumaWyrazow)
stat = {}
wyrazy = a.split()
for slowo in wyrazy:
    ostatnia = slowo[-1].lower()
    if ostatnia in stat:
        stat[ostatnia]+=1
    else:
        stat[ostatnia]=1
for litera, numer in stat.items():
    print(litera,":",numer)
    