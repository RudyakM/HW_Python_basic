from module import Calcilation

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
            result = Calcilation.calc(operand_1, operation, operand_2)
            history = Calcilation.historic(history, operand_1, operation, operand_2, result)
            print(f'\n{operand_1} {operation} {operand_2} = {result}\n')
        
        if input('History? y/n: ') == 'y':
            print(Calcilation.print_history(history))
        if input('Continue? y/n: ') == 'n':
            print('Bye')
            break
