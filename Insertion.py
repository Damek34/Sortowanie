liczby = []


def InsertionSort(liczby, ile):
    for x in range(1, ile):
        wybierz = liczby[x]
        y = x-1

        while y >= 0 and wybierz < liczby[y]:
            liczby[y+1] = liczby[y]
            y -= 1
        liczby[y+1] = wybierz
    return liczby

"""
x - 4
y - 5

jeżeli y >=0 i x < y

y+1 = y 
czyli 4 = 5
y--
y+1 = x
czyli  
"""

print("Ile liczb chcesz posortować?")
ile = int(input())

for i in range(0, ile):
    print("Podaj", i+1, "liczbę")
    liczby.append(input())

liczby = InsertionSort(liczby, ile)
print(liczby)