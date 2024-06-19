from data import MENU,resources
profit = 0

# TODO:2 -- Make a func "report()" to print current data of machine
def report():
    """Print detailed report of machine resources"""
    for ingredient in resources:
        if ingredient == 'coffee' :
            print(f"{ingredient}:{resources[ingredient]}g")
        else:
            print(f"{ingredient}:{resources[ingredient]}ml")

    print(f"Money:${profit}\n")

# TODO:3 -- Make a func "resourse_check()" to check resourses

def resourse_check(coffeeType):
    """Returns TRUE if everything is good"""
    need = coffeeType["ingredients"]
    for ingredient in need:
        if need[ingredient] > resources[ingredient]:
            print(f"\nSorry There's not enough {ingredient}\n")
            return False
        else:
            return True

# TODO:4 -- Make a func "process_coin()" to count total money

def process_coins():
    """Return total amount"""
    quaters = int(input("Enter number of quaters: "))
    dimes = int(input("Enter number of dimes: "))
    nickles = int(input("Enter number of nickles: "))
    pennies = int(input("Enter number of pennies: "))
    total = float ((quaters*0.25) + (dimes*0.10 ) + (nickles*0.05) + (pennies*0.01))
    return total

# TODO:5 -- Make a func "transaction_check()" to check wheater user gives full amount and return change

def transaction_check(coffee,totalMoney):
    """Return FALSE if not enough money"""
    MoneyRequired = coffee['cost']
    if MoneyRequired > totalMoney:
        print("\nSorry That's not enough money. Money refunded\n")
        return False
    elif totalMoney > MoneyRequired:
        print(f"\nHere's is ${round(totalMoney-MoneyRequired,2)} in change\n")
        return True
    else:
        return True


# TODO:6 -- Make a func "make_coffee()" which will deduct and add resourses and profit to machine sytsem

def make_coffee(CoffeeType):
    global profit
    profit += CoffeeType['cost']
    dict_of_ingredients = CoffeeType["ingredients"]
    for ingredient in dict_of_ingredients:
        resources[ingredient]-=dict_of_ingredients[ingredient]

# TODO:1 -- Make a func "coffee_machine()" as a start function which asks for input
def coffee_machine():
    turn_off = False
    print(f"\n{'_'*15} WELCOME TO COFFEE MACHINE {'_'*15}\n ")

    while not turn_off:

        coffee_input = input("Enter what you want ? (espresso,latte,cappuccino) :").lower()

        if coffee_input == 'off':
            turn_off = True
        elif coffee_input == 'report':
            report()
        elif coffee_input == 'refill':
            resources['water'] = 300
            resources['milk'] = 200
            resources['coffee']=100
            print("Machine Refilled\n")
        else:
            GivenCoffeeType = MENU[coffee_input]
            if resourse_check(GivenCoffeeType):
                amount = process_coins()
                if transaction_check(GivenCoffeeType,amount):
                    make_coffee(GivenCoffeeType)
                    print(f"Enjoy your {coffee_input} :) \n")

for coffeeName in MENU:
    ingred_dict = MENU[coffeeName]['ingredients']
    if len(ingred_dict)!=3:
        if 'water' not in ingred_dict:
            ingred_dict['water']=0
        elif 'coffee' not in ingred_dict:
            ingred_dict['coffee'] = 0
        else:
            ingred_dict['milk'] = 0
coffee_machine()




