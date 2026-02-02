lst = ['a', 'b', 'c', 'a']


result = []
current = [lst[0]]

for i in range(1, len(lst)):
    if lst[i] == lst[i - 1]:
        current.append(lst[i])
    else:
        result.append(current)
        current = [lst[i]]

result.append(current)

print(result)
