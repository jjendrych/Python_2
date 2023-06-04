import string
from os import path
import string

"""Otwieranie pliku"""
with open('tekst.txt', 'r') as tekst:
    a = tekst.read()
    suma_wyrazow = len(a.split())
    slowo = (a.split())
    
    print("Suma wyrazów w tekście wynosi: ",suma_wyrazow)
    
    """inicjowanie słownika gdzie beda trzymane ostatnie litery wraz z liczbami"""
    stat = {}
    for i in slowo:
      i = i.strip(string.punctuation + string.whitespace) 
      """usunięcie spacji i interpunkcji"""
      """iterowanie od tyłu żeby dostać ostatnią literę"""
      ostatnia = i[-1]  
      
      if ostatnia in stat:
        stat[ostatnia] += 1
      else:
        stat[ostatnia] = 1
    
    for i1, i2 in stat.items():
        print(i1,":", i2)

