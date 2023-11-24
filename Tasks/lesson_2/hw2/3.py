# Задача про парты(1 парта = 2 школьника, 1 остаток = 1 парта)
x = int(input('1: '))
y = int(input('2: '))
z = int(input('3: '))

class_1 = (x // 2) + (x % 2)
class_2 = (y // 2) + (y % 2)
class_3 = (z // 2) + (z % 2)
result = class_1 + class_2 + class_3

print(result)