#    The greatest number
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

import random

list_digit = [i for i in range(1, 100)]
random.shuffle(list_digit)
len_digit = len(list_digit)

big_int = 0
count = 0
while len_digit > 0:
    if list_digit[count] > big_int:
        big_int = list_digit[count]
    
    count += 1
    len_digit -= 1
print(big_int)
    
