#BUDGET CALCULATOR WITH PYHTHON
#welcome header for user 
from asyncio import transports


print('Welcome to The Simple Budget Calculator!')

#user input
income = float(input('Enter monthly income after taxes($USD): '))
additional = float(input( 'Enter additional monthly income after taxes ($USD): '))

total_income = income + additional 
print('Awesome your total income next month will be ' + str(total_income))
print('Lets gather your exspenses for the month. ')


#user expenses using a function 
def user_expenses(): #this is a funtion called user expenses
    housing = float(input('Enter monthly Housing expenses: '))
    utilities = float(input('Enter all of your monthly utility expenses: '))
    food = float(input('Enter your monthly food expenses (groceries & dining out, $USD): '))
    transportation = float(input('enter your monthly car payment: '))
    cellular = float(input('enter your monthly cell bill: '))

    total_expsenses = housing + utilities + food + transportation + cellular
    return total_expsenses

#calculation of income and expenses 
expense_total = user_expenses()
print('Awesome your total income next month will be ' + str(expense_total))
budget= total_income - expense_total

#if statement to determine what to display as output 
if budget >= 0: 
    print('Your total income surplus next month will be ' + str(budget))
else:
    print('You will be $ ' + str(budget) + 'negative next month!, lets find more income or eliminate some expenses!')
    
    
print('Thank you for using the simple budget calculator!')