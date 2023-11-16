numbers = {
    '+3': '0634167093',
    '+6': '0931010715',
    '+5': '0732990061',
    '+12': '0482526694',
    '+4': '0635167090',
    '+7': '0636167098',
}
result = []
# 1
print('# 1')
print([numbers.get(i) for i in sorted(numbers, key= lambda x: int(x))])


# 2
print('# 2')
print([i for i in sorted(numbers.values(), key= lambda x: int(x), reverse=True)])


# 3
print('# 3')
print([i for i in sorted(numbers.values(), key= lambda x: x[3:])])

# 4
print('# 4')
print([i for i in sorted(numbers.values(), key= lambda x: x[-1])])
