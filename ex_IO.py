
def print_menu():
    print("1. Print phone numbers")
    print("2. Add a phone number")
    print("3. Remove a phone number")
    print("4. Lookup a phone number")
    print("5. Load phone numbers FROM txt file")
    print("6. Save phone numbers INTO txt file")
    print("7. Quit program")
    print()


menu_choice = 0

while True:
    menu_choice = int(input("Type in menu selection number (1-7):"))
    if menu_choice == 1:
        print_numbers(phone_list)
    elif menu_choice == 7:
        break


    