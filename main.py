from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import MenuItem
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
another_coffee='1'

is_on = True
while is_on:
    user_input = input("Type '1' to turn of machine\nType '2' to generate report\nType '3' to order your coffee\n")
    if user_input == '1':
        is_on = False
    elif user_input == "2":
        coffee_maker.report()
        money_machine.report()
    elif user_input=='3':
        while another_coffee=='1':
            order = input(f"What would you like {menu.get_items()}: ")
            drink = menu.find_drink(order)
            if drink != None and coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            choice=input("Type '1' to order another coffee\nType '2' to go back\n")
            if choice=='2':
                break
    else:
        print("Wrong key pressed")
