# Визначте відсоток малих і великих літер у тексті, що зберігається у файлі.
# Використайте функцію isalpha().
# Важливо: читати файл необхідно порядково.

with open('result.txt', 'r') as file:
    lines = file.readlines()
    Small = 0
    Big = 0
    for line in lines:
        for chars in line.strip():
            if chars.isalpha():
                if chars.istitle():
                    Big += 1
                else:
                    Small += 1
                
print(f'all liters {Small + Big}, Big liters {round((Big/(Big+Small))*100)}% Small liters {round((Small/(Big+Small))*100)}%')