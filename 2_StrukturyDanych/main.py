#zadanie1
a=(10,-3,4,9,12,-6,0)
num_min=a[0]
max_num=a[0]
for num in a:
    if num>max_num:
        max_num=num
    elif num<num_min:
        num_min=num

print("Oto twoja krotka:", a)
print("Najmniejsza liczba w krotce:", num_min)
print("Największa liczba w krotce:", max_num)
