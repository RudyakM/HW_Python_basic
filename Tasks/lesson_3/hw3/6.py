# Квадраты натуральных чисел
number = int(input('number: '))
x = 1

while number >= (x ** 2):
    print(x ** 2, end = ' ')
    x += 1

print()