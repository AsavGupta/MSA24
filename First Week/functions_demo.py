#Function to add 2 numbers
#Input (int)number_1, (int) number_2
#Output (int)total
def add_numbers(number_1, number_2):
    c = 7
    return number_1 + number_2
    

def main():
    a = 5
    b = 4
    c = 2
    answer = add_numbers(a,b)
    print(f'{a} + {b} = {answer}')
    print(f'Variable c = {c}')

main()