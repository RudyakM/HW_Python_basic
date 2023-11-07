list = [1, 1.1, 'word', True, False, None]
list_float = [1.1, 2.2, 3.3]
NUMBER = 0
NUMBER_FOR_LIST = 0


def type_in_list(num):
    RESULT = type(list[num])
    return RESULT

def float_in_int(num):
    RESULT = int(list_float[num])
    return RESULT

while NUMBER < len(list_float):
    print(float_in_int(NUMBER))
    NUMBER += 1

while NUMBER_FOR_LIST < len(list):
    result = type_in_list(NUMBER_FOR_LIST)  
    NUMBER_FOR_LIST += 1
    print(result)
