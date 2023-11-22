def calc(operation='+'):
    operation_plus = '+'
    operation_minus = '-'
    operation_mult = '*'

    for _ in operation:
        if _ == operation_plus:
            return lambda x, y: x + y
        elif _ == operation_minus:
            return lambda x, y: x - y
        elif _ == operation_mult:
            return lambda x, y: x * y
        else:
            return lambda x, y: 'something went wrong...'


math_file_way = '/home/maksym/project/Hillel_Python_basic/Tasks/hw15/math.txt'
result_file_way = '/home/maksym/project/Hillel_Python_basic/Tasks/hw15/result.txt'

with open(math_file_way, 'r') as file_math:
    with open(result_file_way, 'w') as file_result:
        for line in file_math:
            equation_list = line.split()
            try:
                result = calc(equation_list[1])
                file_result.write(f'{equation_list[0]} {equation_list[1]} {equation_list[-1]} = {result(int(equation_list[0]), int(equation_list[-1]))}\n')
            except IndexError:
                file_result.write(f'{line} = error\n')
            except ValueError:
                file_result.write(f'{equation_list[0]} {equation_list[1]} {equation_list[-1]} = error\n')
