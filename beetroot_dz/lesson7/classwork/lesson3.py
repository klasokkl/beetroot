import string

def cripted(text: str, key: int)->str:
    ascii2 = string.ascii_letters
    cript = []
    for i in text:
        if i in ascii2:
            cript.append(ascii2[(ascii2.find(i)+key) % len(ascii2)])
        else:
            cript.append(i)
    
    return ''.join(cript)

def decripted(text, key):
    return cripted(text, 52-key)

if __name__ == "__main__":
    print(cripted('Hello World!', 10))
    print(decripted('Rovvy gyBvn!', 10))
