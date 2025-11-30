# Реалізуйте програму, яка зчитує ціле число, що вводиться з командного рядка,
# і записує у текстовий файл інформацію, щодо парності або непарності числа.
# 1. Програма працює поки користувач не закриє її за допомогою команди
# 2. Здійснити запис за допомогою print: число -> парне або не парне
# 3. Один раз викликати відкриття файлу і при закритті програми закрити і сам файл

with open('/home/anton/python/beetroot_dz/beetroot_dz/lesson10/classrwork/file', 'a') as file:
    while True:
        text = input()

        if text == 'exit':
            break
        try:
            print(f'число -> {"парне" if int(text) % 2 == 0 else "непарне"}', file=file)
        except ValueError:
            print('inpyt number! not str')


        