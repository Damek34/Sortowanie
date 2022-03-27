import numpy as np

liczby = []

def MergeSort(liczby):

    if len(liczby) == 1:
        return liczby


    polowa = np.array_split(liczby, 2)
    lewo = polowa[0]
    prawo = polowa[1]










print("Ile liczb chcesz posortować?")
ile = int(input())

for i in range(0, ile):
    print("Podaj", i+1, "liczbę")
    liczby.append(input())

MergeSort(liczby)