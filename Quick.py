liczby = []
def Partition(liczby, lewo, prawo):
    i = lewo - 1
    pivot = liczby[prawo]

    for j in range(lewo, prawo):
         if liczby[j] <= pivot:
             i += 1
             liczby[i], liczby[j] = liczby[j], liczby[i]

    liczby[i+1], liczby[prawo] = liczby[prawo], liczby[i+1]
    return i + 1

def QuickSort(liczby, lewo, prawo):
    if lewo < prawo:
        p = Partition(liczby, lewo, prawo)
        QuickSort(liczby, lewo, p-1)
        QuickSort(liczby, p+1, prawo)
    return liczby




print("Ile liczb chcesz posortować?")
ile = int(input())

for x in range(0, ile):
    print("Podaj", x+1, "liczbę")
    liczby.append(int(input()))

n = len(liczby) - 1
print("Posortowane liczby:")

liczby = QuickSort(liczby, 0, n)
for i in liczby:
    print(i)


