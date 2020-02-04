# Paste your code into this box

guess = 0
response = ""

low = 0
high = 100

print("Please think of a number between 0 and 100!")

while response != "c":
    guess = int((low + high)/2)
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == "h":
        high = guess
    elif response == "l":
        low = guess
    elif response == 'c':
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("Sorry, I did not understand your input.")