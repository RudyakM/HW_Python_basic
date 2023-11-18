from module import calc

history = ''

if __name__ == '__main__':
    while True:
        operand_1 = int(input('Num 1: '))
        operand_2 = int(input('Num 2: '))
        operation = input('Operation: (+, -, *, /, //, %): ')
        
        if operation == '//' and (operand_1 or operand_2) == 0:
            print('Divided by zero') 
            continue
        elif operation not in ('+', '-', '*', '/', '%', '//'): 
            print('Такой операции нет')
            continue
        else:
            result = calc(operand_1, operation, operand_2)
            history += f'{operand_1} {operation} {operand_2} = {result}\n'
            print(f'{operand_1} {operation} {operand_2} = {result}')
        
        if input('History? y/n: ') == 'y':
            print(f'\nHistory:\n{history}')
        if input('Continue? y/n: ') == 'n':
            print('Bye')
            break
