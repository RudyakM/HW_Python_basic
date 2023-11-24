import random

theme = {'sport': ('football', 'basketball', 'voleyball', 'hockey'),
        'fruit': ('apple', 'banana', 'orange', 'pear', 'grapes'),
        'colours': ('red', 'yellow', 'green')
        }

while True:
    user_input = input(f'Выберете тему: {[i for i in theme.keys()]}: ')

    if user_input in theme.keys():
        word = random.choice(theme.get(user_input))
        break
    else:
        print('Такой темы нет. Попробуйте еще раз...\n')
        continue

tries = len(word) * 2
unguess_word = list('_' * len(word))
guessed_word = ''

print('\nYour word:', *unguess_word,
      '\nThe length of your word:', len(word), 
      '\nTotal attempts:', tries, '\n'
      )
    
while True:
    print('\n\nAttempts left:', tries)
    user_input_letter = input('Введите ').lower()
    
    if (user_input_letter.isdigit()) or (len(user_input_letter) > 1) or (len(user_input_letter) == 0):
        print('Нужно ввести только 1 букву...\n')
        continue
    else:
        if tries > 1:
            tries -= 1
            for i in range(len(word)):
                if user_input_letter == word[i]:
                    print(*word[i], end='')
                    unguess_word[i-1] = word[i]  
                else:
                    print(*unguess_word[i-1], end='')
            print()
            
            if '_' not in unguess_word:
                print('\n\nYou Win')
                break
        else:
            print('You Lose...')
            break
