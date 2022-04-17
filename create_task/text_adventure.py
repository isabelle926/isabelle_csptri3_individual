import random
import time


def buildMenu(menu):
    for key, value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")  # each menu item is printed


def presentMenu(menu):
    buildMenu(menu)  # print out menu and take input
    choice = int(input())
    while choice not in menu:  # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func":  # determine whether recursion is needed
            menu[choice]["exec"]()  # run function

        else:
            presentMenu(menu[choice]["exec"])  # display submenu


# dictionaries/lists and variables to be used
inventory = [{
    "Item": "Expired protein bar",
    "Description": "A chocolate-flavored protein bar. It expired in June 2016.",
    "Actions": ["consume", "discard"]
}, {
    "Item": "Grape juice",
    "Description": "A can containing half a liter of grape juice.",
    "Actions": ["consume", "discard"]
}]


# asks user for name, and creates introduction
def introduction():
    username = input("What is your name?")
    print("You wake up to sound of the forest coming alive, with creatures stirring and looking for their next meal.")
    print("You sit up and look around, discovering that your companions have already left.")
    print("There's a note sitting on the ground, and a trail where you can see footsteps. ")
    print("What will you do?")
