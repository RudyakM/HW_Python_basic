def calc(oper='+'):
    if oper == '+':
        return plus()
    else:
        return err()
    
def plus(x=None, y=None):
    return x + y

def err(x=None, y=None):
    return 'Эта операция недопустима!'

# err = calc('^') OMG!!!
calc('^')
assert err(1, 2) == 'Эта операция недопустима!'
