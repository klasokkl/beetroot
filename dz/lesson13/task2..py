#Write a Python program to access a function inside a function (Tips: use function, which returns another function


def add_five(x):
    return x + 5

def do_twice(f):
    def resultin_func(x):
        return f(f(x))
    return resultin_func

resuls = do_twice(add_five)
print(resuls(5))