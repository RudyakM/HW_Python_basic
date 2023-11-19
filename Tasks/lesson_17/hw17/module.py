class Calcilation:

    def __init__(self, operand_1=0, operation='+', operand_2=0):
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operation = operation

    def calc(self):
        operation = self.operation
        operand_1 = self.operand_1
        operand_2 = self.operand_2
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
        
    def historic(self, history, result):
        history += f'{self.operand_1} {self.operation} {self.operand_2} = {result}\n'
        return history

    def print_history(self, history):
        return f'\nHistory:\n{history}'