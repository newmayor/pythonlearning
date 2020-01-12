

def get_questions():
    # notice how the data is stored as a list of lists
    return [["What color is the daytime sky on a clear day? ", "blue"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"],
            ["What does a truly advanced machine make?", "ping"]]

def menu():
    print()
    print("Press t to take the test")
    print("Press L to view the list of questions")
    print("Press Q to quit the program")

def check_question(question_and_answer):
    #extract the question and the answer from the list
    question = question_and_answer[0]
    answer = question_and_answer[1]

    given_answer = input(question)
    #compare the user's answer to the tester's answer
    if answer == given_answer:
        print("correct")
        print()
        return True
    else:
        print("incorrect, correct answer is: ", answer)
        print()
        return False


def run_test(questions):
    if len(questions) == 0:
        print("no questions are given")
        # the return exits the function
        return
    
    index = 0
    correct = 0

    menu()

    menu_select = 0

    while menu_select != 'q':
        menu_select = input("make a menu selection: ")
        while index < len(questions):
            #check the question and extract both question and answer
            if check_question(questions[index]):
                correct = correct + 1
            #go to the next question
            index = index + 1
        #to calculate % grade of correctly answered questions
        print("You got", correct*100 / len(questions), "% right out of", len(questions))
        print()

run_test(get_questions())
