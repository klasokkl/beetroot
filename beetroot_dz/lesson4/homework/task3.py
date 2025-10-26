import random

user_input = list(input('print text: '))
for i in user_input:
    random.shuffle(user_input)
    print(''.join(user_input), end=' ')
