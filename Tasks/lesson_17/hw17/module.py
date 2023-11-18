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

