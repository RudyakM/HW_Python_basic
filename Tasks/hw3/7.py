# Рассчитать сумму последовательности целых чисел
# Программа принимает числа, пока не будет 0 - программа делает вычисления
even = 0
odds = 0
list = []

while True:
    number = int(input())
    if number:
        list.append(number)
        if number % 2 == 0:
            even += 1
        else:
            odds += 1
    
    elif number == 0:
        print(list)
        print(f'Количество введённых чисел: {len(list)}')
        print(f'Сума чисел: {sum(list)}')
        print(f'Среднее арефметическое: {round(sum / len(list), 1)} ')
        print(f'Максимальное значение: {max(list)}')
        print(f'Минимальное значение: {min(list)}')
        print(f'Количество чётных элементов: {even}')
        print(f'Количество не чётных элементов {odds}')
        break