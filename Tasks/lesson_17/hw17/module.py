class Calcilation:

    def __init__(self, item_1=0, operation='+', item_2=0, history=''):
        self.item_1 = item_1
        self.item_2 = item_2
        self.operation = operation
        self.history = history

    def calc(self):
        operation = self.operation
        
        d = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x * y,
             '//': lambda x, y: x * y,
             '/': lambda x, y: x * y,
            }
        
        return d.get(operation)

        
    def historic(self, result):
        self.history += f'{self.item_1} {self.operation} {self.item_2} = {result}\n'
        return self.history

    def print_history(self):
        print(f'\nHistory:\n{self.history}')