#Create a program that accepts a hwy number and outputs the direction
def hwy_direction_decider():
    while True:
        try:
            hwy_number = int(input('\nEnter a Highway number: '))
            if hwy_number < 0:
                print('Please enter a valid highway number')
                continue
        except:
            print('Please enter a valid highway number')
            continue
        print(f'Interstate {hwy_number} runs North to South' if hwy_number % 2 != 0 else f'Interstate {hwy_number} runs East to West')
        if input('Would you like to check another highway? (y/n): ') == 'y':
            continue
        else:
            print('\nEnding program...')
            break

def main():
    hwy_direction_decider()

main()