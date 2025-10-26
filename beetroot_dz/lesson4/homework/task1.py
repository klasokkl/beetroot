import random
user_input = int(input('Guess the number '))
python_input = random.randint(1, 10)
if python_input == user_input:
    print(python_input, 'Your Win')
else:
    print('Your lose', python_input)