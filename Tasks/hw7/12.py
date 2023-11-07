import random 

lst = [random.randint(100, 200) for i in range(10)]
lst.sort(reverse=True)
student_height = int(input('Введите рост ученика: '))
print(lst)

for item in lst:
    if student_height > item:
        lst.insert(lst.index(item), student_height)
        break
    elif student_height == item:
        x = lst.count(item)
        lst.insert(lst.index(item) + x, student_height)

print(lst)

