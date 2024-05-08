MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

LOGO = """
   ______      ________             __  ___           __    _          
  / ____/___  / __/ __/__  ___     /  |/  /___ ______/ /_  (_)___  ___ 
 / /   / __ \/ /_/ /_/ _ \/ _ \   / /|_/ / __ `/ ___/ __ \/ / __ \/ _ \
/ /___/ /_/ / __/ __/  __/  __/  / /  / / /_/ / /__/ / / / / / / /  __/
\____/\____/_/ /_/  \___/\___/  /_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/        
"""

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# function 1
def generateReport(resources:dict, profit: str):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    return f"Money: ${profit}"

# function 2
def checkResources(userOrder:str, MENU:dict):
    order = MENU[userOrder]
    orderIngredients = order['ingredients']
    
    if not ( orderIngredients['water'] <=  resources['water'] and orderIngredients['milk'] <=  resources['milk'] and orderIngredients['coffee'] <=  resources['coffee']):
        return f"Sorry there is not enought resources"
    return ""

# function 4
def reduceResources(order:str):
    # After payment reduce total resources
    global resources
    resources['water'] -= MENU[order]['ingredients']['water']
    resources['milk'] -= MENU[order]['ingredients']['milk']
    resources['coffee'] -= MENU[order]['ingredients']['coffee']
    
    
# function 3
def validatePayment(userOrder:str):
    global profit
    order = MENU[userOrder]
    orderCost = float(order['cost'])
    
    print("Please insert coins :^) : ")
    
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes? ")) 
    nickles = int(input("How many nickles? "))
    pennies =  int(input("How many pennies? "))
    
    payment = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(payment, " ", orderCost)
    
    if float(payment) >= float(orderCost):
        profit += orderCost
        reduceResources(userOrder)
        return f"Here is ${payment - orderCost} in Change"
    else:
        return f"Sorry that's not enough money. Money refunded"


def handleUserRequest(userOrder:str):
    if userOrder == 'report':
        global profit
        return generateReport(resources, profit)
    else:
        # first validate resources
        resource_check_result = checkResources(userOrder, MENU)
        if resource_check_result:
            return resource_check_result
        # validate Payment
        return validatePayment(userOrder)

def coffeeMachine(MENU, resources):
    # Indicate system start
    print(LOGO)
    
    userOrder = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    
    while (userOrder != ''):
        if userOrder not in ("espresso", "latte", "cappuccino", "report"):
            return "System Exit"
        
        result = handleUserRequest(userOrder)
        if result:
            print(result)
        
        userOrder = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        
    return f"Total Profit: ${profit}"


print(coffeeMachine(MENU, resources))