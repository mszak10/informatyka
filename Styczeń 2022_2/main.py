# Zadanie 4 - Wykreślanka

with open("pliki/wykreslanka.txt") as file:
    fileContent = file.read()
    fileContent = fileContent.split('\n')
    # print(len(fileContent))

    for i, linia in enumerate(fileContent):
        if 'matura' in linia:
            index = linia.find("matura")
            print(f'{i}')

    rotated = []
    newline = ''
    for i in range(len(fileContent)):
        newline = ''
        for j in range(len(fileContent)):
            newline += fileContent[j][i]
        rotated.append(newline)

# print(rotated)
print('===============')

for i, linia in enumerate(rotated):
    if 'matura' in linia:
        index = linia.find("matura")
        print(f'{i}') # missing 199