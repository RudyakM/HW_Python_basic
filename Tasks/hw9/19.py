lst = input('Введите: ').lower().replace(',', '').replace('.', '').split()
dicter = dict.fromkeys(lst, 0)

for word in dicter:
    dicter[word] = lst.count(word)
    print(word, ':', dicter[word])