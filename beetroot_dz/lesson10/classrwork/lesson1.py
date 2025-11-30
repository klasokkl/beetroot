sum = 0
with open('/home/anton/python/beetroot_dz/beetroot_dz/lesson10/classrwork/file', 'r') as file:
    for line in file:
        sum += int(line)

with open('/home/anton/python/beetroot_dz/beetroot_dz/lesson10/classrwork/file2', 'w') as file:
    file.write(str(sum))