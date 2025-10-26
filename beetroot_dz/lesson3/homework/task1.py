in_text = input('print words: ')
if len(in_text) <= 1:
    print('Empty String')
else:
    print(in_text[:2]+in_text[-2:])