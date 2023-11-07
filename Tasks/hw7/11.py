import random

lst = [random.randint(1,20) for _ in range(20)]
print(lst)
x = [1 for item in range(1, len(lst) - 1) if lst[item] > lst[item - 1] and lst[item] > lst[item + 1]]   
print(sum(x))