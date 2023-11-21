history = ''

while True:
    operand_1 = int(input('Число 1: '))
    operand_2 = int(input('Число 2: '))
    operation = input('Введите операцию (+, -, *, /, //, %): ') 
    if operation == '+':
        result = operand_1 + operand_2
        history += f'{operand_1} + {operand_2} = {result}\n'
        print(f'Результат: {result}') 
    elif operation == '-':
        result = operand_1 - operand_2
        history += f'{operand_1} - {operand_2} = {result}\n' 
        print(f'Результат: {result}') 
    elif operation == '*':
        result = operand_1 * operand_2
        history += f'{operand_1} * {operand_2} = {result}' 
        print(f'Результат: {result}') 
    elif operation == '/':
        result = operand_1 / operand_2
        history += f'{operand_1} / {operand_2} = {result}\n' 
        print(f'Результат: {result}') 
    elif operation == '%':
        result = operand_1 % operand_2
        history += f'{operand_1} % {operand_2} = {result}\n' 
        print(f'Результат: {result}') 
    elif operation == '//' and (operand_2 and operand_1) != 0:
        result = operand_1 // operand_2
        history += f'{operand_1} // {operand_2} = {result}\n' 
        print(f'Результат: {result}') 
    elif (operand_1 or operand_2) == 0:
        print('На ноль делить незьзя...') 
        continue
    else: 
        print('Такой операции нет...')
        continue

    historic = input('\nПоказать историю y/n: ')
    if historic == 'y':
        print(f'\nHistory:\n{history}\n')

    continuer = input('Хотите продолжить y/n: \n')
    if continuer == 'n':
        print('Bye')
        break


    
