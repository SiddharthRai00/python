import random

jackpot = (random.randint(1,100))
guess = int(input('guess the number :'))
counter = 1

while guess !=jackpot:

    if  guess > jackpot:
        print('GUESS A LITTLE LOWER!! :')

    else :
        print('GUESS A LITTLE HIGHER :')

    guess = int(input('guess the number again :'))
    counter +=1
else:
    print('congrats!! you guessed right')
    print('total attempts:',counter)