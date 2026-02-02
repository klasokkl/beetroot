
class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    MARKUP = 0.30  # наценка магазина 30%

    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("Количество должно быть положительным")

        # Добавляем наценку
        product.price *= (1 + self.MARKUP)

        if product.name in self.products:
            self.products[product.name]["amount"] += amount
        else:
            self.products[product.name] = {
                "product": product,
                "amount": amount,
                "discount": 0
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Скидка должна быть от 0 до 100")

        found = False

        for info in self.products.values():
            product = info["product"]

            if (identifier_type == 'name' and product.name == identifier) or \
               (identifier_type == 'type' and product.type == identifier):
                info["discount"] = percent
                found = True

        if not found:
            raise ValueError("Продукты с указанным идентификатором не найдены")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Продукт не найден")

        info = self.products[product_name]

        if amount <= 0 or amount > info["amount"]:
            raise ValueError("Недостаточно товара на складе")

        price = info["product"].price
        discount = info["discount"]

        final_price = price * (1 - discount / 100)

        self.income += final_price * amount
        info["amount"] -= amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [
            (name, data["product"].type, data["product"].price,
             data["amount"], data["discount"])
            for name, data in self.products.items()
        ]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError("Продукт не найден")

        info = self.products[product_name]
        return (product_name, info["amount"])


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
