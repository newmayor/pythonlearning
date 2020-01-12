number = 7 
guess = -1

print('Enter a number guess! ')
while guess != number:
    guess = int(input('Enter a your guess: '))

    if guess == number:
        print("you got it!")
    elif guess < number:
        print("goe higher!")
    elif guess > number:
        print("go lower!")