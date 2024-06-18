def main():
    menu = {"Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}
    
    total = 0
    while True:
        ordered_item = input('\nItem: \n').title()
        if ordered_item.lower() == 'end':
            break
        try:
            total += menu[ordered_item]
            print(f'Total: ${(total):.2f}')
        except:
            continue

main()
