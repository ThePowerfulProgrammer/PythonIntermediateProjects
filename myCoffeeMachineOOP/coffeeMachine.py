'''Model the Coffee Machine

Contains: 
    resources 
    Menu
    profit
'''
class CoffeeMachine(object):
    

    def __init__(self) -> None:
        self.resources = {
            'water': 300,
            'milk': 300,
            'coffee': 100,
        }       
    
    # display current resources
    def getReport(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}mg")
        return ""

        
    # if resources sufficient, make sale and reduce internal resources
    def isResourcesSufficient(self,drink):
        canMake = True
        for ingridient in drink.ingredients:
            if (drink.ingredients[ingridient] > self.resources[ingridient]):
                print(f"{ingridient} is insufficent")
                canMake = False
        return canMake
    
    # user selected drink, user pays, machine accepts, and change if any are returned 
    def makeCoffee(self,drink):
        for ingridient in drink.ingredients:
            self.resources[ingridient] -= drink.ingredients[ingridient]
        print(f"Here is your {drink.name} ☕️. Enjoy!")
        
    
        
    
