def calc(operation='+'):
    if operation == '+':
        return plus()
    elif operation == '-':  
        return minus()
    elif operation == '*':  
        return multiply()
    else:
        return err()

def plus(x=None, y=None):
    return lambda x, y: x + y

def minus(x=None, y=None):
    return lambda x, y: x - y

def multiply(x=None, y=None):
    return lambda x, y: x * y

def err(x=None, y=None):
    return lambda x, y: 'something went wrong...'


with open('/home/maksym/project/HW_Python_basic/Tasks/hw15/math.txt', 'r') as file_math:
    with open('/home/maksym/project/HW_Python_basic/Tasks/hw15/result.txt', 'w') as file_result:
        for line in file_math:
            lst = line.split()
            try:
                calculater = calc(lst[1])
                file_result.write(f'{lst[0]} {lst[1]} {lst[-1]} = {calculater(int(lst[0]), int(lst[-1]))}\n')
            except IndexError:
                file_result.write(f'{line} = error\n')
            except ValueError:
                file_result.write(f'{lst[0]} {lst[1]} {lst[-1]} = error\n')
