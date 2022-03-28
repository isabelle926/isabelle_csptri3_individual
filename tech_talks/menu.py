from trees import christmasTrees
from cafe import coolCafe
from ships import coolShips
from lists_dictionaries import InfoDb, for_loop, while_loop, recursive_loop, fibonacci
from cool_classes import dispfac, dispSeries, superfac, printpal


def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("Welcome to Felix's Flea Market! Where would you like to shop? If you'd like to see Isabelle's other TT challenges, go to the submenu. ") # user input prompt


def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu


tt1menu = {
    1: {
        "display":"Hack 2a (for loop)",
        "exec": for_loop,
        "type":"func"
    },
    2: {
        "display":"Hack 2b (while loop)",
        "exec": while_loop,
        "type":"func"
    },
    3: {
        "display":"Hack 2c (recursive)",
        "exec": recursive_loop,
        "type":"func"
    },
    4: {
        "display":"Hack 3 (fibonacci)",
        "exec": fibonacci,
        "type":"func"
    },
    5: {
        "display":"Quit program",
        "exec": quit,
        "type":"func"
    },
}

tt2menu = {
    1: {
        "display":"Factorial Calculator",
        "exec": dispfac,
        "type":"func"
    },
    2: {
        "display":"Factorial series",
        "exec": dispSeries,
        "type":"func"
    },
    3: {
        "display":"Superfactorial",
        "exec": superfac,
        "type":"func"
    },
    4: {
        "display":"Palindrome",
        "exec": printpal,
        "type":"func"
    },
    5: {
        "display":"Quit program",
        "exec": quit,
        "type":"func"
    },
}

mainMenu = {
    1: {"display":"Tracy's Tall Trees",
        "exec":christmasTrees,
        "type":"func"},
    2: {"display":"Cathy's Café",
        "exec":coolCafe,
        "type":"func"},
    3: {"display":"Suzanne's Ships",
        "exec":coolShips,
        "type":"func"},
    4: {"display":"TT1 Submenu ",
        "exec":tt1menu,
        "type":"func"},
    5: {"display":"TT2 Submenu ",
        "exec":tt2menu,
        "type":"func"},
    6: {"display":"Quit Program",
        "exec":quit,
        "type":"func"}
}

if __name__ == "__main__":
    while True: #forever loop
        presentMenu(mainMenu)
        halt = input("Do you want to continue (y/n)? ") #checks if user wants to go again
        if halt.lower() == "n":
            break