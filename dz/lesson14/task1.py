
def func_decorator(f):
    def wrapper(*args, **kwargs):
        #print('start')
        #result = f(*args, **kwargs)
        #print('stop')

        return f, *args, *kwargs
    return wrapper

@func_decorator
def add(a, b):
    return a + b

@func_decorator
def square(a):
    return a ** 2

print(add(10, 3))