def main():
    #Capitalize String
    my_name = 'Asav'
    print(my_name.capitalize())

    #Make a string Uppercase
    print(my_name.upper())

    #Make it lowercase
    last_name = 'GUPTA'
    print(f'{my_name.capitalize()} {last_name.lower()}')

    #Determine if a string starts with a set of characters
    print(my_name.startswith("a"))

    if(not my_name.startswith("a") and not my_name.startswith('A')):
        print('You spelled my name wrong')
    else:
        print('You spelled my name correctly')

    #Determine if a string ends with a specific set of character
    print(my_name.endswith("sav"))

    #Find a set of characters in a string
    print(my_name.find("a", 7))
    
    #loop through a string
    print('\n\n')
    for letter in my_name:
        print(letter)

    print(f'{my_name} has {len(my_name)} letters')

    for letter_index in range(len(my_name)):
        print(f'Letter {letter_index+1}: {my_name[letter_index]}')
    
    print('\n\n')
    
    sentence = 'I have a dog. My dog is cute. Do you want a dog?'
    #write code that counts the number of times dog is in the sentence

    number_of_dogs = 0
    start_index = 0
    while True:
        dog_index = sentence.find("dog", start_index)
        if dog_index == -1:
            break
        else:
            number_of_dogs +=1
            start_index = dog_index + 1
            continue

    print(f'The number of dogs in the sentece was {number_of_dogs}')

    #How to use the split method
    car_info = "Ferrari,f-50,2021,500000,4.8"
    
    car_data = car_info.split(',')
    print(car_data)

main()