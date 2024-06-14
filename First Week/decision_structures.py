def main():
    
    a = 5
    b = 5
    if a > b:
        print(f'{a} is greater than {b}')
    elif b > a:
        print(f'{b} is greater than {a}')
    else:
        print(f'{a} and {b} are equal')
    
    #Print appropriate letter grade based on the test score
    #A: 100-90
    #B: 89-80
    #C: 79-70
    #D: 69-60
    #F: 59-0
    test_score = 60 #float(input('Enter your test score: '))
    print('\nGrade Decision: 1')

    if test_score <= 100 and test_score >= 90:
        print(f'{test_score} --> A')
    elif test_score <= 90 and test_score >= 80:
        print(f'{test_score} --> B')
    elif test_score <= 80 and test_score >= 70:
        print(f'{test_score} --> C')
    elif test_score <= 70 and test_score >= 60:
        print(f'{test_score} --> D')
    else:
        print(f'{test_score} --> F')

    print('\nGrade Decision: 2')

    if test_score >= 90:
        print(f'{test_score} --> A')
    elif test_score >= 80:
        print(f'{test_score} --> B')
    elif test_score >= 70:
        print(f'{test_score} --> C')
    elif test_score >= 60:
        print(f'{test_score} --> D')
    else:
        print(f'{test_score} --> F')

    #Create structure to decide the seasons based on the month
    #Winter: 12, 1, 2 - Spring: 3, 4, 5 - Summer: 6, 7, 8 - Fall: 9, 10, 11
    #Ask user for month number, then output the season based on the month

    while True:
        try:
            month_number = int(input('Enter the number of the current month (Jan = 1): '))
            if month_number > 12 or month_number < 1:
                 print('Please enter a number between 1 and 12')
            else:
                break
        except:
            print('Please enter a number between 1 and 12')

    if month_number in [12,1,2]:
        print('The month is Winter')
    elif month_number in [3,4,5]:
        print('The month is Spring')
    elif month_number in [6,7,8]:
        print('The month is Summer')
    elif month_number in [9,10,11]:
        print('The month is Fall')


main()