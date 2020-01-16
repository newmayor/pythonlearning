

def print_numbers(numbers):
    print("These are the currently stored phone numbers: ")
    for k, v in numbers.items():
        print("Name:", k, "\tNumber:", v)
    print()

def add_number(numbers, name, number):
    numbers[name] = number #use a dict to define name as the dict key and the associated number as the dict value

def remove_number(numbers, name):
    if name in numbers:
        del numbers[name]
    else:
        print(name, " was not found")

def lookup_number(numbers, name):
    if name in numbers:
        return "The number belonging to " + name + "is " + numbers[name]
    else:
        return name + " was not found."

def load_numbers(numbers, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()

def save_numbers(numbers, filename):
    out_file = open(filename, "wt")
    for k, v in numbers.items():
        out_file.write(k + ", " + v + "\n")
    out_file.close()

def print_menu():
    print("1. Print phone numbers")
    print("2. Add a phone number")
    print("3. Remove a phone number")
    print("4. Lookup a phone number")
    print("5. Load phone numbers FROM txt file")
    print("6. Save phone numbers INTO txt file")
    print("7. Quit program")
    print()

phone_list = {}
menu_choice = 0
print_menu()

while True:
    menu_choice = int(input("Type in menu selection number (1-7):"))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 2:
        print("Adding a name and number to the phonebook.")
        name = input("Name?: ")
        phone = input("Enter the phone number: ")
        add_number(phone_list, name, phone)
    elif menu_choice == 3:
        print("Remove a name and associated number.")
        name = input("Name of the phone number to remove? ")
        remove_number(phone_list, name)
    elif menu_choice == 4:
        print("Looking up a number")
        name = input("Enter the name of the person whose phone number you want to lookup: ")
        print(lookup_number(phone_list, name))
    elif menu_choice == 5:
        print("Loading phone numbers from a txt file...")
        filename = input("Please enter the file name or path to load:")
        load_numbers(phone_list, filename)
    elif menu_choice == 6:
        print("Saving the numbers to a txt file...")
        filename = input("Enter the filename or path to which you'd like to save these numbers to: ")
        save_numbers(phone_list, filename)
    elif menu_choice == 7:
        break
    else:
        print_numbers

print("Goodbye!")


    