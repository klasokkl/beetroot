from lesson10_files.phonebook_app.helper import read_values


def create_record(database: dict) -> dict:
    new_record = read_values()
    database.update(new_record)
    return database


def update_record(database: dict) -> dict:
    print('Введіть номер телефону та дані, які потрібно оновити (решту можна пропустити)')
    new_record = read_values(update=True)
    for phone, data in new_record.items():
        for key, value in data.items():
            if value:
                database[phone][key] = value
    return database


def delete_record(database: dict) -> dict:
    phone = input("Введіть номер телефону, який хочете видалити: ")
    result = database.pop(phone, None)
    if result:
        print('Номер телефону видалено')
    else:
        print('Номер телефону не знайдено')
    return database


if __name__ == '__main__':
    print(create_record({}))
    print(update_record(
            {"0987654321": {'first_name': 'John', 'last_name': 'Doe', 'city': 'San Francisco', 'country': 'USA'}}
        )
    )
