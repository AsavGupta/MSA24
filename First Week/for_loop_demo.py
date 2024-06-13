def main():
    #Print Integers between 0 and 10
    for i in range(11):
        print(i)

    #print integers between 5 and 10
    print('\n\n')
    for i in range(5,11):
        print(i)

    #print even numbers between 0 and 10
    print('\n\n')
    for i in range(0,11,2):
        print(i)
    
    #prompt the user for start and top values and print the numbers between start and stop
    while True:
        try:
            start_value = int(input('Enter a start value: '))
            stop_value = int(input('Enter a stop value: '))
            if(start_value >= stop_value):
                print('Start Value should be less than Stop Value')
            else:
                for i in range(start_value,stop_value+1):
                    print(i)
                break
        except:
            print("Enter an Integer")
main()