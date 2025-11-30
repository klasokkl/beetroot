#Write a Python program to detect the number of local variables declared in a function.



def func_locall():
    a = 1
    b = 2
    c = 3
    d = 4
    return len(locals())

print(func_locall())
