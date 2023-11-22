def custom_abs(n):
   if n > 0:
      return n
   elif n < 0:
      return abs(n)
   else:
      return str(n)


assert custom_abs(-15) == 15
assert custom_abs(-201) == 201
assert custom_abs(20) == 20
assert custom_abs(1) == 1
assert custom_abs(0) == '0'