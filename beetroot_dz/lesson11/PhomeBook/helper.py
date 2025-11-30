from collections import defaultdict

base_dict = {'phone_number': {
    'first_name': 'John',
    'last_name': 'Doe',
    'city': 'San Francisco',
    'country': 'United States'
}}

keys = ['phone_number', 'first_name', 'last_name', 'city', 'country']
values = ['номер телефону', 'ім\'я', 'прізвище', 'місто', 'країна']
names = dict(zip(keys, values))


def help_text():
    print(
        'Доступні команди:',
        'n - створити новий запис',
        'sf - пошук за імененем',
        'sl - пошук за прізвищем',
        'sfl - пошук за ім\'ям та прізвищем',
        'sp - пошук за номером телефону',
        'sct - пошук за містом',
        'sc - пошук за країною',
        'up - оновлення запису',
        'del - видалення запису',
        'help - виведння списку команд',
        'exit - завершення роботи програми',
        sep='\n'
    )


def print_values(data: dict) -> None:
    for phone, data in data.items():
        for key, value in names.items():
            if key == 'phone_number':
                print(f'{value.capitalize()}: {phone}')
            else:
                print(f'\t{value.capitalize()}: {data[key]}')
        print('-' * 30)


def read_values(update=False) -> dict:
    if not update:
        print('Натисніть ENTER щоб залишити значення порожнім')
    result = defaultdict(dict)
    phone = ''
    for key, value in names.items():
        if key == 'phone_number':
            phone = input(f'Введіть {value}: ')
        else:
            data = input(f'Введіть {value}: ')
            result[phone][key] = data
    return result


if __name__ == '__main__':
    print_values(base_dict)
    print(read_values())