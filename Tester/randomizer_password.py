import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
BIG_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'
SPEC_SYMBOLS = '!@#$%^&?<>()+-_=8'
result = ''

while True:
    lenght = int(input('\nWhat length? - '))
    use_letter = input('Use letter? y/n: ')
    use_big_letter = input('Use big letter? y/n: ')
    use_digits = input('Use digits? y/n: ')
    use_spec_symbol = input('Use spec symbol? y/n: ')

    while len(result) < lenght:
        symbol_randomizer = random.randint(1, 4)
        if use_letter == 'y' and symbol_randomizer == 1:
            result += random.choice(LETTERS)
        elif use_big_letter == 'y' and symbol_randomizer == 2:
            result += random.choice(BIG_LETTERS)
        elif use_digits == 'y' and symbol_randomizer == 3:
            result += random.choice(DIGITS)
        elif use_spec_symbol == 'y' and symbol_randomizer == 4:
            result += random.choice(SPEC_SYMBOLS)
    print(f'\nPassword: {result}\n')
    
    breaker = input('Continue? y/n: ')
    if breaker == 'n':
        print('Bye')
        break
    else:
        continue
