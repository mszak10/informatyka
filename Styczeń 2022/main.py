# Wyznacz liczbę miast w której powstają galerie

# Zadanie 4.1
kraje = {}
with open("galerie.txt") as plik:
    for linia in plik:
        kraj = linia.split(" ")[0]
        if kraj in kraje:
            kraje[kraj] += 1
        else:
            kraje[kraj] = 1
with open("wynik4_1.txt.txt", 'w') as plik:
    for kraj in kraje:
        plik.write(kraj + " " + str(kraje[kraj]) + "\n")

# Zadanie 4.2
with open("galerie.txt") as plik:
    maximum = ['First', 0]
    minimum = ['Last', 10000]
    for linia in plik:
        a = count = 0
        linia = linia.split(" ")
        miasto = linia[1]
        for i in range(3, len(linia), 2):
            a += int(linia[i-1]) * int(linia[i])
            if int(linia[i-1]) * int(linia[i]) > 0:
                count += 1
        if a > maximum[1]:
            maximum[0] = miasto
            maximum[1] = a
        elif a <= minimum[1]:
            minimum[0] = miasto
            minimum[1] = a
        # print(f"{miasto} {a} {count}")
        with open("wynik4_2a.txt", 'a') as p:
            p.write(miasto + " " + str(a) + " " + str(count) + "\n")
    with open("wynik4_2b.txt", 'a') as r:
        r.write(f'{maximum[0]} {maximum[1]}\n')
        r.write(f'{minimum[0]} {minimum[1]}')
