lst_1 = set(input("Введите 1-ю последовательность целых чисел разделенных пробелом: ").split())
lst_2 = set(input("Введите 2-ю последовательность целых чисел разделенных пробелом: ").split())

result = sorted(lst_1.intersection(lst_2))

print(['Уникальных чисел нет!', f'{len(result)} ==> ' + ' '.join(result)][len(result) > 0])