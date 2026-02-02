
class Dog:
    
    def __init__(self, age, age_factor=7):
        self.age = age
        self.age_factor = age_factor

    def human_age(self):
        print(f'human age {self.age * self.age_factor}')

dog = Dog(3)
dog.human_age()

