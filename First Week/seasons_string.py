def main():

    while True:    
        month_number = input("Enter month numbner 1 - 12: ")

        if month_number in ['12','1','2']:
            print('The month is Winter')
        elif month_number in ['3','4','5']:
            print('The month is Spring')
        elif month_number in ['6','7','8']:
            print('The month is Summer')
        elif month_number in ['9','10','11']:
            print('The month is Fall')
        else:
            print("Please enter a number between 1 and 12")
            continue
        break

main()