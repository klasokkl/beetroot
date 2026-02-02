
class Person:
    
    def __init__(self, name, a_name, age):
        self.name = name
        self.a_name = a_name
        self.age = age

    def talk(self):
        print(f'Hello my name is {self.name} {self.a_name} and {self.age} years old')


a = Person('Jon', 'Snow', '99')
a.talk()