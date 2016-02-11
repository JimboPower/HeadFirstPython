def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

print(sorted(sanitize(each_t) for each_t in james))
print(sorted(sanitize(each_t) for each_t in julie))
print(sorted(sanitize(each_t) for each_t in mikey))
print(sorted(sanitize(each_t) for each_t in sarah))

ciao = james[0:3]

print(ciao)

print(james[0:5])


unique_james = []

for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)

print(unique_james[0:3])

"""Reverse these number"""
numbers = ['3', '1', '7', '9']
numbers.sort(reverse=False)
print(numbers)





