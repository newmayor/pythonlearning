from random import randint

number = randint(0, 99)
guess = -1

while guess != number:
    guess = int(input('guess again! '))
    if guess == number:
        print('you got it right! ')
    elif 0 <= guess < number:
        print('a little bit higher! ')
    elif guess > number:
        print('go a little bit lower! ')
