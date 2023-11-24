def calc(operation='+'):
    operation_plus = '+'
    operation_minus = '-'
    operation_mult = '*'

    for _ in operation:
        if _ == operation_plus:
            return lambda x, y: x + y
        elif _ == operation_minus:
            return lambda x, y: x - y
        elif _ == operation_mult:
            return lambda x, y: x * y
        else:
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