'''Model the MenuItems'''

class MenuItem(object):
    
    '''name, cost,ingredients'''
    def __init__(self, name, cost, water,milk,coffee) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water":water,
            "milk":milk,
            "coffee":coffee,
        }
        

'''Models the Menu'''
class Menu(object):
    
    # Set the Menu
    def __init__(self) -> None:
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),   
        ]
        
    # display the Menu
    def getMenu(self) -> None:
        items = ''
        for item in self.menu:
            items += f'{item.name}/'
        return items
        
    # cross check User's order
    def findDrink(self,drink) -> bool:
        for item in self.menu:
            if (drink == item.name):
                return item
        return False
    
            
        
    