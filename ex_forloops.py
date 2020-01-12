print("try to guess my name")
count = 1
name = "numair"
guess = input("first try to guess my name: ")

while count <=3 and guess.lower() != name:
    print("You are wrong!")
    guess = input("What is my name?")
    count += 1

if guess.lower() != name:
    print("you are wrong!")
    print("youve run out of chances")
else:
    print("yes! my name is ", name + "!")