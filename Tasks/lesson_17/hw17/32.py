from module import calc

history = ''

if __name__ == '__main__':
    while True:
        operand_1 = int(input('Число 1: '))
        operand_2 = int(input('Число 2: '))
        operation = input('Введите операцию (+, -, *, /, //, %): ')
        
        if operation == '//' and (operand_1 or operand_2) == 0:
            print('На ноль делить незьзя...') 
            continue
        elif operation not in ('+', '-', '*', '/', '%', '//'): 
            print('Такой операции нет...')
            continue
        else:
            result = calc(operand_1, operation, operand_2)
            history += f'{operand_1} {operation} {operand_2} = {result}\n'
            print(f'{operand_1} {operation} {operand_2} = {result}')
        
        if input('Показать историю y/n: ') == 'y':
            print(f'\nHistory:\n{history}')
        if input('Хотите продолжить y/n: ') == 'n':
            print('Bye')
            break
