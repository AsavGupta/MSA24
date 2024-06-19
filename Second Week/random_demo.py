import random

def main():

    #print a random number bewtween 1-10
    print('Random number: 1-10')
    random_value = random.randint(1,10)
    print(f'Random Value: {random_value}')

    #Generate 10 random numbers between 1 and 10
    print('\nRandom 10 numbers: 1-10\n-----------')
    for i in range(10):
        print(f'Random Number {i+1}: {random.randint(1,10)}')

    #Choose a random value from a list of values
    print('\nChoose random value from list\n-----------')
    rand_list = [4,7,10,23,44,18,9,12]
    random_index = random.randint(0,len(rand_list)-1)

    print(f'Random Index: {random_index}')
    print(f'Random list value: {rand_list[random_index]}')

    #ask a user for the start and stop values to generate a random number between
    #ask the user how many random numbers to generate, and generate that many numbers
    print('\nUser Generated Random Numbers\n-----------')
    start_value = int(input("What's your start value?: "))
    stop_value = int(input("What's your stop value?: "))
    generation_count = int(input("How many numbers do you want to generate?: "))
    for i in range(generation_count):
        print(f'Random Number {i+1}: {random.randint(start_value,stop_value)}')


main()