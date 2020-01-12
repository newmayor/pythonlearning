max_points = [25, 25, 50, 25, 100]
assignments = ['hw ch 1', 'hw ch 2', 'quiz  ', 'hw ch 3', 'test']
students = {'#Max': max_points}

def print_menu():
    print('1. add student')
    print('2. remove student')
    print('3. print grades')
    print('4. record grade')
    print('5. print menu')
    print('6. exit')

def print_all_grades():
    print('\t', end= ' ')
    for i in range(len(assignments)):
        print(assignments[i], '\t', end=' ')
    print()
    keys = list(students.keys())
    keys.sort()
    for x in keys:
        print(x, '\t', end=' ')
        grades = students[x]
        print_grades(grades)

def print_grades(grades):
    for i in range(len(grades)):
        print(grades[i], '\t', end=' ')
        print(grades[i])
    print()

print_menu()
menu_choice = 0

while menu_choice != 6:
    print()
    menu_choice = int(input("enter menu choice 1-6: "))

    if menu_choice == 1:
        name = input("enter a new name to add: ")
        students[name] = [0]*len(max_points)
    elif menu_choice == 2:
        name = input("enter name to remove: ")
        if name in students:
            del students[name]
        else:
            print("Student: ", name, "not found. ")
    elif menu_choice == 3:
        print_all_grades()
    elif menu_choice == 4:
        print('record new grade input: ')
        name = input("enter the name of the student for the new grade input: ")
        if name in students:
            grades = students[name]
            print('type in the number of the grade to input for this student: ')
            print('press 0 [zero] to exit... ')
            for i in range(len(assignments)):
                print(i + 1, assignments[i], '\t', end=' ')
            print()
            print_grades(grades)
            which = 1234
            while which != -1:
                which = int(input("change which grade: "))
                which -= 1
                if 0 <= which < len(grades):
                    grade = int(input('enter the grade: '))
                    grades[which] = grade
                elif which != -1:
                    print('invalid grade number. ')
        else:
            print('student not found! ')
    elif menu_choice != 6:
        print_menu()