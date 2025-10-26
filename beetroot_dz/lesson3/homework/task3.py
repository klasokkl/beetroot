while True:
    calc = input('Print task: ')
    if calc == "break":
        break

    try:
        print(eval(calc))
    except:
        print('error in expression')
    
