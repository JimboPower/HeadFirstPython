data = open('sketch.txt')

data.seek(0)

for line in data:
    (role, line_spoken) = line.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(line_spoken, end='')
