def calc(operator='+'):
    def err(*input_data):
        return 'something went wrong'
    
    d = {'+': lambda x, y: x + y,
         '-': lambda x, y: x - y,
         '*': lambda x, y: x * y,
        }
    
    if operator in d:
        return d.get(operator)
    else:
        return err


math_file_way = '/home/maksym/project/Hillel_Python_basic/Tasks/hw15/math.txt'
result_file_way = '/home/maksym/project/Hillel_Python_basic/Tasks/hw15/result.txt'

with open(math_file_way, 'r') as file_math:
    items = [line.strip() for line in file_math.readlines() if len(line.strip()) > 0]
    result_lst = []

    for item in items:
        try:
            item_1, operator, item_2 = map(str.strip, item.split())
            item_1, item_2 = int(item_1), int(item_2)
            result = calc(operator)(item_1, item_2)
        except Exception:
            output = f'{item} = error'
        else:
            output = f'{item} = {result}'
        result_lst.append(output)  
with open(result_file_way, 'w') as file_result:
    file_result.write('\n'.join(result_lst))