from typing import final


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# check if resources are sufficient or not 

def resource_sufficient (order_item) :
    if MENU[their_order]['ingredients']['water'] <= resources['water'] and MENU[their_order]['ingredients']['coffee'] <= resources['coffee']:
        if order_item == 'espresso':
            print('everything is suffiecient')
            insert_coins(order_item)
        else:
            if MENU[their_order]['ingredients']['milk'] <= resources['milk']:
                print('everything is suffiecient') 
                insert_coins(order_item)
    else :
        print('resources are not sufficient for making the coffie')
        


# give the user coffie and reduce the resource

def give_them_coffie(order_item):
    print(f'here is your {order_item} E N J O Y !!')

    resources['water'] = resources['water'] - MENU[order_item]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[order_item]['ingredients']['coffee']
    if order_item != 'espresso':
        resources['milk'] = resources['milk'] - MENU[order_item]['ingredients']['milk']

    
        
    


# insert coins

def insert_coins(order_item) :
    print('Please insert coins.')

    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))

    price  = 0.25 * quarters + 0.10  * dimes + 0.05 * nickles + 0.01 * pennies 
    if price >= MENU[order_item]['cost']:
        change = round(price - MENU[order_item]['cost'], 2)
        print(f'here is your ${change}')
        give_them_coffie(order_item)
    else :
        print(f'This amt is not sufficient to drink {order_item}')
    



on = True

while on :

    their_order = input('What would you like? (espresso/latte/cappuccino): ')

    # check resources if resources is sufficient then ask for money
    resource_sufficient(their_order)

    # ask to insert coins 



    
    
















