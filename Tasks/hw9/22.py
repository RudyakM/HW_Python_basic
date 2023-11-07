lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']
lst = []
d = {}
result = {}

# здесь продолжайте программу (используйте список lst_in)
lst += [item.split() for item in lst_in]

for key, value in lst:
    d.setdefault(key, value)

for value, key in d.items():
    result.setdefault(key, [])
    result[key].append(value)

# вывод результатов
print(result)