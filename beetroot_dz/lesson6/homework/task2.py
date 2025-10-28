#Generate 2 lists with the length of 10 with random integers from 1 to 10,
#  and make a third list containing the common integers between the 2 initial lists without any duplicates.
#Constraints: use only while loop and random module to generate numbers

import random

list_a = [i for i in range(1, 11)]
list_b = [i for i in range(1, 20)]

random.shuffle(list_a)
random.shuffle(list_b)

list_c = set(list_a + list_b)
print(list_c)