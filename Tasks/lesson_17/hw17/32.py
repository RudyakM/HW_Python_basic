from module import Calcilation

history = ''
if __name__ == '__main__':
    while True:
        item_1 = int(input('Num 1: '))
        item_2 = int(input('Num 2: '))
        operation = input('Operation: (+, -, *, /, //, %): ')
        
        if operation == '//' and (item_1 or item_2) == 0:
            print('Divided by zero') 
            continue
        elif operation not in ('+', '-', '*', '/', '%', '//'): 
            print('Такой операции нет')
            continue
        else:
            pointer = Calcilation(item_1, operation, item_2, history)
            result = pointer.calc()(item_1, item_2)
            history = pointer.historic(result)
            print(f'\n{item_1} {operation} {item_2} = {result}\n')
        
        if input('History? y/n: ') == 'y':
            pointer.print_history()
        if input('Continue? y/n: ') == 'n':
            print('Bye')
            break
        