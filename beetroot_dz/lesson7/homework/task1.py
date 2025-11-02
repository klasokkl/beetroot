#Make a program that has some sentence 
# (a string) on input and returns a dict containing all unique 
# words as keys and the number of occurrences as values. 

words = input()

dict_words = {}

for word in words.split():
    dict_words[word] = dict_words.get(word, 0) + 1

print(dict_words)