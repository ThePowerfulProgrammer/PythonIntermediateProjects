from coffeeMachine import CoffeeMachine
from menu import Menu
from moneyMachine import MoneyMachine


CONTINUE = True

menu = Menu()
coffeeMachine = CoffeeMachine()
money_machine = MoneyMachine()

while CONTINUE:
    options = menu.getMenu()
    choice = input(f"What would you like {options}: ")
    if choice == 'off':
        print("Have a nice day")
        print(f"Total profit: ${money_machine.profit}")
        CONTINUE = False 
    elif choice == 'report':
        print(coffeeMachine.getReport())
    else:
        drink = menu.findDrink(choice)
        
        if (coffeeMachine.isResourcesSufficient(drink) and money_machine.make_payment(drink.cost)):
            # make sale
            coffeeMachine.makeCoffee(drink)
            
            
        