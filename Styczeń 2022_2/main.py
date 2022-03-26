# Zadanie 4 - Wykreślanka

print('4.1')
with open("pliki/wykreslanka.txt") as file:
    fileContent = file.read()
    fileContent = fileContent.split('\n')

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
        print(f'{i}')  # warn missing 199

print('4.2')
with open("pliki/wykreslanka.txt") as file:
    result = 0
    fileContent = file.read()
    fileContent = fileContent.split('\n')
    c = 1
    rows = []
    for i, linia in enumerate(fileContent):
        for j in range(len(fileContent)):
            while True:
                if fileContent[i][j] == fileContent[i][j + 1]:
                    c += 1
                    break
                else:
                    if c == result:  # DEBUG: to be checked
                        rows.append(i)
                    elif c > result:
                        result = c
                        rows.clear()
                        rows.append(i)
                    c = 1
                    break
    print(result, rows)
