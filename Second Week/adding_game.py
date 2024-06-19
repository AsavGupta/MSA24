import random

#Determine Difficulty
def difficulty(): 
    while True:
        try:
            dif_level = int(input("Enter Level 1, 2, 3: "))
            if dif_level in [1,2,3]:
                return dif_level
            else:
                print("Error: Invalid Input!")
        except:
            print("Error: Invalid Input!")

#Determine Number of Questions
def question_amount():
    while True:
        try:
            questions = int(input("Enter number of questions to ask: 3 to 10: "))
            if questions in range(3,11):
                return questions
            else:
                print("ERROR: Please enter an integer value between 3 and 10!")
        except:
            print("ERROR: Please enter an integer value between 3 and 10!")

def question_asker(diff):
    if diff == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    if diff == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    if diff == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return ([x,y,x+y])

def main(): 
    #Call Functions 
    game_difficulty = difficulty()
    num_of_questions = question_amount()
    number_of_tries = 3
    questions_asked = 0
    questions_right = 0

    while questions_asked < num_of_questions:

        #Difficulty Setting and Asking questions
        question_values = question_asker(game_difficulty)

        #Check for tries
        attempts=0
        questions_asked+=1
        while attempts < number_of_tries: 
            try:
                if int(input(f'\n{question_values[0]} + {question_values[1]} = ')) != question_values[2]:
                    print('WRONG!!')
                    attempts+=1
                    if attempts == number_of_tries:
                        print(f'Correct Answer: {question_values[2]} ')
                else:
                    questions_right+=1
                    print('CORRECT!!')
                    break
            except:
                continue

    grade = (questions_right/questions_asked)*100
    print(f'\nYou got {questions_right} out of {questions_asked} correct: {grade:.2f}%')            

main()