array = input('')
values = array.split(' ')
print(values)

mn = min(values)
firstElementIndex = 0

while firstElementIndex < (len(values) - 1) and values[firstElementIndex] > mn:
    print(firstElementIndex)
    values[firstElementIndex] = mn
    firstElementIndex += 1
    mn = min(values[firstElementIndex : ])
    

print(values)

