# Определить наибольший целый квадрат числа(100 = 10, 101 = 10, 3 = 1)
n = int(input('n: '))
k = 1

while n >= (k ** 2): 
    if n // k == k:     
        print(k)
    elif n // k == n < (k + 1) ** 2:
        print(k)
    k += 1

