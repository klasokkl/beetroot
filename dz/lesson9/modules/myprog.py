
def count_lines(name)-> int:
    with open(name, 'r') as file:
        return len(file.readlines())
    

def count_char(name) -> int:
    with open(name, 'r') as file:
        count = 0
        for i in file.readlines():
            count += len(i)

        return count

def test(name):
    print(count_lines(name))
    print(count_char(name))