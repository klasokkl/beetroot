

class Product:

    def __init__(self, name, price):
        self.name = name
        self._price = price


    @property
    def price(self):
        return f'{self._price} UAH'
    

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError('')
        if value <= 0:
            raise ValueError('gg')
        
    
if __name__ == "__main__":
    b = Product('banan', 100)
    print(b.price)