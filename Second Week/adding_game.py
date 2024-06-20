import random

#Determine Difficulty
def difficulty(): 
    while True:
        try:
            dif_level = int(input("\nEnter Level 1, 2, 3: "))
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
            questions = int(input("\nEnter number of questions to ask: 3 to 10: "))
            if questions in range(3,11):
                return questions
            else:
                print("ERROR: Please enter an integer value between 3 and 10!")
        except:
            print("ERROR: Please enter an integer value between 3 and 10!")

#Determine Question Values
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

    #Call Functions and Set Vars
    game_difficulty = difficulty()
    num_of_questions = question_amount()
    number_of_tries = 3
    questions_asked = 0
    questions_right = 0
    total_attempts = 0
    right_answer_responses = ['CORRECT!!', 'YESSIR', 'SKIBIDI', 'W']
    wrong_answer_responses = ['WRONG!!', 'DUMMY', 'WHAT THE SIGMA', 'L', 'Keep Yourself Safe!', 'You\'re Adopted']

    #Game Loop
    while questions_asked < num_of_questions:

        #Difficulty Setting and Asking questions
        question_values = question_asker(game_difficulty)

        #Check for tries
        attempts = 0
        questions_asked+=1

        while attempts < number_of_tries:
            total_attempts+=1 
            try:
                if input(f'\n{question_values[0]} + {question_values[1]} = ') != str(question_values[2]):
                    #Random Responses
                    print(wrong_answer_responses[random.randint(0,len(wrong_answer_responses)-1)])
                    attempts+=1
                    if attempts == number_of_tries:
                        #If Out of Guesses
                        print(f'Correct Answer: {question_values[2]} ')
                else:
                    questions_right+=1
                    #Random Responses
                    print(right_answer_responses[random.randint(0,len(right_answer_responses)-1)])
                    break
            except:
                attempts+=1
                print(wrong_answer_responses[random.randint(0,len(wrong_answer_responses)-1)])
                continue
    
    #Grading
    grade = (questions_right/questions_asked)*100
    total_grade  = (questions_right/total_attempts)*100
    print(f'\nYou got {questions_right} out of {questions_asked} correct: {grade:.2f}%')    
    print(f'\nYou got {questions_right} out of {total_attempts} total attempts correct: {total_grade:.2f}%')           

main()
