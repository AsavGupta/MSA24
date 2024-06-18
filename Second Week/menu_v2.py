#Func to load menu items from the file menu.txt and create a dictionary
#Input: None
#Output: Dictionary of menu items
def get_menu_items():

    #create a file handler that gives us access to the file
    data_file = open("menu.txt", "r")

    #create an empty dictionary to store menu items and prices
    menu_items = {}

    #loop through data in the file and read the file one line at a time 
    for line_of_data in data_file:       

        #split the line of data at the comma using .split()
        keys_and_values = line_of_data.split(',')

        # get item and price from the resulting list and store and store in the dictionary 
        item = keys_and_values[0]
        price = float(keys_and_values[1])
        menu_items[item] = price

    #close the file
    data_file.close()
    return menu_items

def main():

    #load the menu items dictionary
    menu_items = get_menu_items()   

    total = 0

    while True:
        ordered_item = input('\nItem: \n').title()
        if ordered_item.lower() == 'end':
            break
        try:
            #check and get the price from the order
            total += menu_items[ordered_item]
            print(f'Total: ${(total):.2f}')
        except:
            continue

main()