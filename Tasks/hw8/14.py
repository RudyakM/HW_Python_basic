import random

lst = [random.randint(1, 200) for _ in range(20)]
mnoj = set(lst)
print(mnoj)
print(len(mnoj))