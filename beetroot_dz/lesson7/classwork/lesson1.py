morse = {'A': '· –', 'B': '– · · ·', 'W': '· – –', 'G': '– – ·', 'D': '– · ·', 'E': '·', 'V': '· · · –', 'Z': '– – · ·',
         'I': '· ·', 'J': '· – – –', 'K': '– · –', 'L': '· – · ·', 'M': '– –', 'N': '– ·', 'O': '– – –', 'P': '· – – ·',
         'R': '· – ·', 'S': '· · ·', 'T': '–', 'U': '· · –', 'F': '· · – ·', 'H': '· · · ·', 'C': '– · – ·',
         'Q': '– – · –', 'Y': '– · – –', 'X': '– · · –'}

print('exit print !q')
while True:
    word = input('print world ')

    if word == 'q!':
        print('exit')
        break
        
    for letter in word.upper():
        print(morse.get(letter, letter), end=' ')

    print()
        