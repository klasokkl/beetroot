#Extracting numbers.
#Make a list that contains all integers from 1 to 100, then 
# find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
#Constraint: use only while loop for iteration

list_a = [i for i in range(1, 101)]

list_b = []
len_list = len(list_a)

count = 0
while len_list > 0:
    value = list_a[count]
    if value % 7 == 0 and value % 5 != 0:
        list_b.append(value)

    count +=1
    len_list -=1
    
print(*list_b)