def main():
    amount_due = 50
    change_values = ['1','5','10','25']
    print('----------')
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        coin_amount = input('Insert Coin:\n')
        if coin_amount  in change_values:
            coin_value = int(coin_amount)
        else:
            coin_value = 0
        if coin_value >= amount_due:
            change = coin_value - amount_due
        amount_due -= coin_value
    print(f'Change Owed: {change}')

main()