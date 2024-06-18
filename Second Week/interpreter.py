def main():
    while True:
        expression = input("Expression: ").split(" ")
        try:
            x = float(expression[0])
            y = expression[1]
            z = float(expression[2])
            if y in ['+','-','*','/']:
                if y == '+':
                    print(x+z)
                elif y == '-':
                    print(x-z)
                elif y == '*':
                    print(x*z)
                elif y == '/':
                    if z == 0:
                        print('ERROR: Cannot divide by 0')
                    print(x/z)
                if input('Would You like to make another calculation (y/n): ') == 'n':
                    break
        except:
            continue

main()