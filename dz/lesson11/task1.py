
def create_file(name, data):
    with open(name, 'w') as file:
        file.write(data)

def read_file(name):
    with open(name, 'r') as file:
        print(file.read())


create_file('my_file', 'hello\n hello\nhi')
read_file('my_file')