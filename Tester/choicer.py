import random


theme = {'sport': ('football', 'basketball', 'voleyball'),
        'fruit': ('apple', 'banana', 'orange'),
        'colours': ('red', 'yellow', 'green')
        }

print(theme['sport'])
print(type(theme['sport']))
word = random.choice(theme.get('sport'))
print(word)