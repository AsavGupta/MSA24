def main():
    #list demo
    #create a list of string names
    names = ["Jonh", "Mary","Alice", "Bob"]
    numbers = [10,16,24,42,14,9]
    rand_list = ["Cyd", 10, 22.3, "Frank"]

    #add values to list
    names.append("Johnny")
    numbers.append(5)
    numbers.append(63)

    print(names, numbers, rand_list)

    print('\n\n')

    #get the number of items in a list
    print(f"Number of Items in my list: {len(numbers)}")

    print('\n\n')


    #Get values from our list
    for i in numbers:
        print(i)

    print('\n\n')

    for index in range(len(numbers)):
        print(f'Index {index+1}: {numbers[index]}')

main()