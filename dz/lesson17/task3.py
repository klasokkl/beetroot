from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()  # скорочуємо дріб при створенні

    def _reduce(self):
        """Скорочення дробу через gcd"""
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        # робимо знаменник завжди додатнім
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    # Магічні методи для арифметики
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    # Магічні методи порівняння
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    # Магічні методи для зручності
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# ====== Тестування ======
if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))  # True
    print(Fraction(2, 4) == Fraction(1, 2))  # True, скорочення працює
