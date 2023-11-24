# Игра угадай число
import random

while True:
    first_nums = int(input('Диапазон от: '))
    second_nums = int(input('Диапазон до: '))
    DIGITS = random.randint(first_nums, second_nums)
    ATTEMPTS = 0

    while True:
        ATTEMPTS += 1
        user_number = int(input('Your number? '))
        
        if DIGITS == user_number:
            print('\nYou win!\n')
            break
        elif user_number > DIGITS:
            print('Попробуй число поменьше')
        else:
            print('Попробуй число побольше')
        
        if ATTEMPTS == 10: 
            print('Попытки закончились')
            break
    
    continuer = input('Продолжаем? y/n: ')
    if continuer == 'n':
        print('Bye')
        break
    
        