d = {'apple': ['malum', 'pomum', 'popula'],
     'fruit': ['baca', 'bacca', 'popum'],
     'punishment': ['malum', 'multa']
    }

result = {}

for word, lst in d.items():
    for item in lst:
        result.setdefault(item, [])
        result[item].append(word)

for item in result:
    print(f'{item}: {result[item]}')

