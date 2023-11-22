lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
    ]
result = []

for item in lst:
    for i in item:
        if type(i) == str:
            item.remove(i)
    
    if item[-1] * item[-2] < 100:
       item[-1] += 10
    result.append(item)

print(list(map(lambda x: tuple(x), result)))
