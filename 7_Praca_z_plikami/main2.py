from os import path
import random
from typing import List

"""Dodanie encoding pozwala na ominięcie błędu UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 64: character maps to <undefined>"""
with open('imiona.txt','r',encoding='utf-8') as names:
    first_name=names.readlines()
    
with open('nazwiska.txt','r',encoding='utf-8') as surnames:
    last_name=surnames.readlines()
    
combinations = int(input("Podaj ile chcesz wygenerować kombinacji imion i nazwisk: "))

"""Dodanie adnotacji, że options to lista, która przechowuje napisy, bo inaczej jest błąd"""
options: List[str] = []

while len(options) < combinations:
    """dodanie nowych zmiennych first_name_option aby różniły się od powyższych, stworzonych przy otwieraniu plików"""
    first_name_option = random.choice(first_name).strip()
    last_name_option = random.choice(last_name).strip()
    option= f"{first_name_option} {last_name_option}"
    
    if option not in options:
        options.append(option)

for i in range(len(options)):
    print(options[i])

    