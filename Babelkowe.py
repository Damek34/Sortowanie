
liczby = []
zapas = 0

def babel(ile, liczby):
    for x in range(0, ile):
        for y in range(x+1, ile):
            if liczby[x] > liczby[y]:
                zapas = liczby[y]
                liczby[y] = liczby[x]
                liczby[x] = zapas
    return liczby





print("Ile liczb chcesz wprowadzić?")
ile = int(input())

for x in range(0, ile):
    print("Podaj", x+1, "liczbę")
    liczby.append(int(input()))

babel(ile, liczby)

"""
for n in range(0, ile):
    for i in range(n+1, ile):
        if liczby[n] > liczby[i]:
            zapas = liczby[i]
            liczby[i] = liczby[n]
            liczby[n] = zapas


"""

print("\n\n")
for x in range(0, ile):
    print(liczby[x])

