import numpy as np
from time import sleep
import time

menu_options = {
    1: "Tracy's Tall Trees",
    2: "Cathy's Café",
    3: "Suzanne's Ships",
    4: "Exit",
}


# Print menu options from dictionary key/value pair
def main_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    runOptions()


# submenus
# menu option 1
def trees():
    print("Welcome to Tracy's Tall Trees!")
    print("Due to the shipment problems, all we have in stock are leftover Christmas trees.")
    a = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])

    for line in a:
        print('  '.join(map(str, line)))

    treeHeight = int(input("How tall would you like your Christmas Tree to be?"))
    christmasTree(treeHeight)
    print("Thanks for shopping with us, bye!")
    exit()


def christmasTree(n):
    z = n - 1
    x = 1
    for i in range(0, n):
        for i in range(0, z):
            print(' ', end='')
        for i in range(0, x):
            print('+', end='')
        for i in range(0, z):
            print(' ', end='')
        x = x + 2
        z = z - 1
        print()


# menu option 2
def cafe():
    print("Welcome to Cathy's Café!")
    for key in submenu_options.keys():
        print(key, '--', submenu_options[key])
    runSubOptions()


submenu_options = {
    1: "Coffee",
    2: "Cake",
    3: "Tea",
    4: "Exit",
}


def coffee():
    print("One hot cup of coffee coming up!")

    def progress(percent=0, width=30):
        # The number of hashes to show is based on the percent passed in. The
        # number of blanks is whatever space is left after.
        hashes = width * percent // 100
        blanks = width - hashes

        print('\r[', hashes * '#', blanks * ' ', ']', f' {percent:.0f}%', sep='',
              end='', flush=True)

    print('This will take a moment')
    for i in range(101):
        progress(i)
        sleep(0.1)

    # Newline so command prompt isn't on the same line
    print()
    print("Your coffee is ready! Enjoy!")
    exit()


def cake():
    print("I'll let you bargain for the cake. How much do you want to pay?")
    x = 0
    y = "cake"
    print("You have: {}".format(x))
    print("Tracy has: {}".format(y))

    x = int(input("Your offer:"))

    if x < 25:
        print("No way. Goodbye")
        exit()
    else:
        temp = x
        x = y
        y = temp

    print("You get: {}".format(x))
    print("Tracy gets: {}".format(y), "dollars")
    exit()


def tea():
    print("")


def runSubOptions():
    while True:
        try:
            option = int(input("What would you like to get?"))
            if option == 1:
                coffee()
            elif option == 2:
                cake()
            elif option == 3:
                tea()
            # Exit menu
            elif option == 4:
                print('Exiting! Thank you! Good Bye...')
                exit()  # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


# menu option 3
def ships():
    print("Welcome to Suzanne's Ships!")
    print("Right now, we have a lovely sailboat in stock.")
    print("Would you like to buy it?")
    answer = input("Enter yes or no: ")
    if answer == "yes":
        print("Sure thing!")
        print("Would you like to sail it now?")
        answer2 = input("Enter yes or no: ")
        if answer2 == "yes":
            ANSI_CLEAR_SCREEN = u"\u001B[2J"
            ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
            OCEAN_COLOR = u"\u001B[44m\u001B[2D"
            SHIP_COLOR = u"\u001B[32m\u001B[2D"
            RESET_COLOR = u"\u001B[0m\u001B[2D"

            def ocean_print():
                # print ocean
                print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
                print("\n\n\n\n")
                print(OCEAN_COLOR + "  " * 35)

            # print ship with colors and leading spaces
            def ship_print(position):
                print(ANSI_HOME_CURSOR)
                print(RESET_COLOR)
                sp = " " * position
                print(sp + "    |\   ")
                print(sp + "    |/   ")
                print(SHIP_COLOR, end="")
                print(sp + "\__ |__/ ")
                print(sp + " \____/  ")
                print(RESET_COLOR)

            # ship function, iterface into this file
            def ship():
                # only need to print ocean once
                ocean_print()

                # loop control variables
                start = 0  # start at zero
                distance = 60  # how many times to repeat
                step = 2  # count by 2

                # loop purpose is to animate ship sailing
                for position in range(start, distance, step):
                    ship_print(position)  # call to function with parameter
                    time.sleep(.1)

            ship()
            exit()
        elif answer2 == "no":
            print("Alright, see you soon!")
            exit()
        else:
            print("Please enter yes or no.")

    elif answer == "no":
        print("Goodbye")
        exit()
    else:
        print("Please enter yes or no.")


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input("Welcome to Felix's Flea Market! Where would you like to shop? "))
            if option == 1:
                trees()
            elif option == 2:
                cafe()
            elif option == 3:
                ships()
            # Exit menu
            elif option == 4:
                print('Exiting! Thank you! Good Bye...')
                exit()  # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')


if __name__ == '__main__':
    main_menu()
