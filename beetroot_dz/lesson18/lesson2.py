# Створити клас Rectangle з автоматичним перерахунком площі
# Створіть клас з атрибутами width і height, area.
# Додайте властивість area, що рахується автоматично.
# Зробіть так, щоб змінюючи ширину або висоту, area оновлювалася.
#
# Підказка: area має бути тільки для читання.


class Rectangle:

    def __init__(self, witdh, height):
        self._witdh = witdh
        self._height = height
        self._area = witdh * height

    @property
        