# Wyznacz liczbę miast w której powstają galerie

kraje = {}
with open("Styczeń 2022/galerie.txt") as plik:
    for linia in plik:
        kraj = linia.split(" ")[0]
        if kraje.__contains__(kraj):
            kraje[kraj] += 1
        else:
            kraje[kraj] = 1
with open("Styczeń 2022/4_1.txt", 'w') as plik:
    for kraj in kraje:
        plik.write(kraj + " " + str(kraje[kraj]) + "\n")
