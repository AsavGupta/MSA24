#Ask users for hours worked
def positive_float():
    while True:
        try:        
            hours = float(input('Enter the number of hours worked daily: '))
            if hours < 0 or hours > 24:
                print('Enter values between 0 and 24 hours')  
            else:
                break            
        except:
            print('Enter values between 0 and 24 hours')
    while True:
        try:
            wage = float(input('Enter the hourly wage: '))
            if wage < 0:
                print('Enter values above $0')
            else:
                print('IN ELSE STATEMENT')
                break
        except:
            print('Enter values above $0')
    return hours,wage

#Run Input
hours,wage = positive_float()

#Calculate Values for Pay Advice
working_days_per_year = 350
tax_percent = .12

yearly_wage_before_tax = hours*wage*working_days_per_year
tax_amount = yearly_wage_before_tax*tax_percent
annual_wage = yearly_wage_before_tax-tax_amount

#Print Pay Advice
print('\nPay Advice')
print('-------------')
print(f'Hours Worked: {hours:.2f}')
print(f'Hourly Wage: ${wage:.2f}')
print(f'Wages Before Taxes: ${yearly_wage_before_tax:.2f}')
print(f'Tax Amount: ${tax_amount:.2f}')
print(f'Annual Wage After Taxes: ${annual_wage:.2f}')





