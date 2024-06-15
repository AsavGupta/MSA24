def ask_coin():
    while True:
        try:
            coin_amount = int(input('Insert Coin:\n'))
            if coin_amount not in [1,5,10,25]:
                return 0
            else:
                return coin_amount
        except:
            return 0

def main():
    amount_due = 50
    print('----------')
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        coin_value = ask_coin()
        if coin_value >= amount_due:
            change = coin_value - amount_due
        amount_due -= coin_value
    print(f'Change Owed: {change}')
main()