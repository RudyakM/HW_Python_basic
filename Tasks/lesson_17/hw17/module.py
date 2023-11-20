class Calcilation:

    def __init__(self, operand_1=0, operation='+', operand_2=0, history=''):
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operation = operation
        self.history = history

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
        
    def historic(self, result):
        self.history += f'{self.operand_1} {self.operation} {self.operand_2} = {result}\n'
        return self.history

    def print_history(self):
        print(f'\nHistory:\n{self.history}')