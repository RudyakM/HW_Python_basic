def rec(n):
    if n > 1:
        return n * rec(n-1)
    else:
        return 1
    
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

print(fib(6))
print(rec(4))