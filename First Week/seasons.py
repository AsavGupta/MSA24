#Create Function to return the season based on the month
#Input: month number
#Output season name

def main():
    while True:
        season = decide_season(get_season_number())
        print(f'The season is {season}')
        #ask user if they want to continue
        if input("Would you like to run again? (y/n): ") == 'n':
            break
        continue
    

def get_season_number():
    while True:
        try:
            month_number = int(input('Enter the number of the current month (Jan = 1): '))
            if month_number > 12 or month_number < 1:
                print('Please enter a number between 1 and 12')
                continue
            break
        except:
            print('Please enter a number between 1 and 12')
    return month_number

def decide_season(month):
    if month in [12,1,2]:
        return 'Winter'
    elif month in [3,4,5]:
        return 'Spring'
    elif month in [6,7,8]:
        return 'Summer'
    elif month in [9,10,11]:
        return 'Fall'

main()