# Write a Python program to construct the following pattern, using a while loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Передбачити задання довжини вершини (максимальної кількості зірочок)

while True:
    inser_text = input()
    if inser_text == 'exit':
        break
    else:
        peak = int(inser_text)
    counter = 0 
    while peak:
        peak -= 1
        counter += 1
        print('*' * counter)
    while counter:
        counter -= 1
        if counter == 0:
            break
        print('*' * counter) 