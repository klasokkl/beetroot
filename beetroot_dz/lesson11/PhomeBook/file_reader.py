import json


def read_database(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return {}
    return data


def write_database(filename, data):
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


if __name__ == "__main__":
    filename = '/home/anton/python/beetroot_dz/beetroot_dz/lesson11/PhomeBook/database/phonebook.json'
    read_database(filename)

