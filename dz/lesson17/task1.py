
class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print('hhhhh')


class Cat(Animal):
    def talk(self):
        print('mmmmm')


def run(cat, dog):
    cat.talk()
    dog.talk()

a = Dog()
b = Cat()
run(a, b)