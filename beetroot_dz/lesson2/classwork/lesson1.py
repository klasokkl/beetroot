while True:
    contry = input()
    if contry == 'exit':
        break
    if contry.isalpha():
        print(contry.capitalize())
