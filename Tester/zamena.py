word = 'banana'
unguess_word = list('_' * len(word))

while True:
    user_input_letter = input('Введите ').lower()
    
    for i in range(len(word)):
        if user_input_letter == word[i]:
            print(*word[i], end='')
            unguess_word[i-1] = word[i]  
        else:
            print(*unguess_word[i-1], end='')
    print()
