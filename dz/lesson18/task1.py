import re


class User:
    def __init__(self, email: str):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email: str):
        if not isinstance(email, str):
            raise TypeError("Email должен быть строкой")

        # Базовая, но надёжная проверка email
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(pattern, email):
            raise ValueError(f"Некорректный email адрес: {email}")

user1 = User("john.doe@gmail.com") 
#user2 = User("john.doe@gmail") 
