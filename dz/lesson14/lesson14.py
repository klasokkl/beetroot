import time

def time_function(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + " took " + str((end - start) * 1000) + "ms")
        return result
    return wrapper

@time_function
def square_numbers(num_list):
    new_list = []
    for num in num_list:
        new_list.append(num**2)
    return new_list

my_list = [1, 2, 3, 4, 5]
my_list_squared = square_numbers(my_list)
print(my_list_squared)