

print("Type control C or -1 to exit")
number = 1
while number != -1:
    try:
        number = int(input("Enter your number: "))
        print("You entered the number: ", number)
    except ValueError:
        print("That was not a number...")