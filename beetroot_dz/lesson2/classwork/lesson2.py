# Write a python program, which sums all digits in a python string.
# Examples, input - '1234', output - 10
# Передбачити перевірку наявності символів в рядку

print(sum([int(i) for i in input() if i.isdigit()]))