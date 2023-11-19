class Calcilation:

    def calc(operand_1, operation, operand_2):
        if operation == '+':
            result = operand_1 + operand_2
            return result 
        elif operation == '-':
            result = operand_1 - operand_2 
            return result 
        elif operation == '*':
            result = operand_1 * operand_2
            return result 
        elif operation == '/':
            result = operand_1 / operand_2 
            return result 
        elif operation == '%':
            result = operand_1 % operand_2
            return result 
        else:
            result = operand_1 // operand_2 
            return result
        
    def historic(history, operand_1, operation, operand_2, result):
        history += f'{operand_1} {operation} {operand_2} = {result}\n'
        return history

    def print_history(history):
        return f'\nHistory:\n{history}'