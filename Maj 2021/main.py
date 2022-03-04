# Otworzenie pliku
instrukcje = []
with open("Dane_2105/instrukcje.txt") as plik:
    # with open("Dane_2105/przyklad.txt") as plik:
    for linia in plik:
        instrukcja = linia.strip()
        instrukcje.append(instrukcja)

print("Zadanie 4:")
# Zadanie 1
length = 0
for ins in instrukcje:
    if ins.startswith("DOPISZ"):
        length += 1
    elif ins.startswith("USUN"):
        length -= 1
print("1:", length)

# Zadanie 2
c_type = None
c_len = 0
max_type = None
max_len = 0
for ins in instrukcje:
    typ = ins.split()[0]
    if not c_type:
        c_type = typ
        c_len = 1
        continue
    if c_type == typ:
        c_len += 1
        if c_len > max_len:
            max_len = c_len
            max_type = c_type
    else:
        c_type = typ
        c_len = 1

print("2:", max_type, max_len)

# Zadanie 3
litery = {}
for ins in instrukcje:
    typ, znak = ins.split()
    if typ == "DOPISZ":
        if znak in litery:
            litery[znak] += 1
        else:
            litery[znak] = 1

najlitera = None
ilelitera = 0
for litera in litery:
    if litery[litera] > ilelitera:
        najlitera = litera
        ilelitera = litery[litera]

print("3:", najlitera, ilelitera)

# Zadanie 4

napis = ""
for ins in instrukcje:
    typ, znak = ins.split()
    if typ == "DOPISZ":
        napis += znak
    elif typ == "ZMIEN":
        napis = napis[:-1] + znak
    elif typ == "USUN":
        napis = napis[:-1]
    elif typ == "PRZESUN":
        if znak == "Z":
            n_znak = "A"
        else:
            asciicode = ord(znak)
            n_znak = chr(asciicode + 1)
        napis = napis.replace(znak, n_znak, 1)

print("4:", napis)
