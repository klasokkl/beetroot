# Створити абстрактну базу даних, що містить 3 класи, основний користувач,
# та два можливих профілі (читач або редактор)

class User:
    
    def __init__(self, login: str, password: str, access=""):
        self.login = login
        self.possword = password
        self.access = access 


class Reader(User):

    def setaccess(self, access="r"):
        self.access = access

class Redactor(User):
    
    def setaccess(self, access="rw"):
        self.access = access



user = Redactor('user','passwr')
user.setaccess()
print(user.access)