def calc(operation='+'):
    if operation == '+':
        return plus()
    elif operation == '-':  
        return minus()
    elif operation == '*':  
        return multiply()
    else:
        return err()

def plus(x=None, y=None):
    return lambda x, y: x + y
def minus(x=None, y=None):
    return lambda x, y: x - y
def multiply(x=None, y=None):
    return lambda x, y: x * y
def err(x=None, y=None):
    return lambda x, y: 'Эта операция недопустима!'



# Test #01
plus = calc('+')
assert plus(10, 20) == 30

# Test #02
minus = calc('-')
assert minus(0, 10) == -10

# Test #03
multiply = calc('*')
assert multiply(-10, 20) == -200

# Test #04
err = calc('some')
assert err(10, 20) == 'Эта операция недопустима!'