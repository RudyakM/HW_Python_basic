def calc_metrics(lst):
   return f'Min value = {str(min(lst))}, max value = {str(max(lst))}, sum = {str(sum(lst))}'


lst = [1, 2, 3, 4, 5, 6]
assert calc_metrics(lst) == 'Min value = 1, max value = 6, sum = 21'

lst = [20, -49, 28, 80, -9, 7, 48, -1, 16, 2]
assert calc_metrics(lst) == 'Min value = -49, max value = 80, sum = 142'

lst = [-48, 48]
assert calc_metrics(lst) == 'Min value = -48, max value = 48, sum = 0'

lst = [11, -3, 2, -1, 8]
assert calc_metrics(lst) == 'Min value = -3, max value = 11, sum = 17'

lst = [10, 20, 30, 40, 50]
assert calc_metrics(lst) == 'Min value = 10, max value = 50, sum = 150'

lst = [-22, -25, -28, -17, -25, -36, -28, -32, -12, -16]
assert calc_metrics(lst) == 'Min value = -36, max value = -12, sum = -241'

lst = [0, 0, 0, 0]
assert calc_metrics(lst) == 'Min value = 0, max value = 0, sum = 0'

lst = [2]
assert calc_metrics(lst) == 'Min value = 2, max value = 2, sum = 2'