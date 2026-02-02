def pascal(n):
    row = [1]
    value = 1

    for k in range(n):
        value = value *(n-k) // (k+1)
        row.append(value)
    
    return row

val = int(input())
for i in range(val):
    print(*pascal(i))
