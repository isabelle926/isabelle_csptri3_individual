# from menu import presentMenu
import numpy as np


def christmasTrees():
    print("Welcome to Tracy's Tall Trees!")
    print("Due to the shipment problems, all we have in stock are leftover Christmas trees.")
    a = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])

    for line in a:
        print('  '.join(map(str, line)))

    n = int(input("How tall would you like your Christmas Tree to be?"))
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

    b = input("Would you like to buy more trees? (type y or n): ")
    if b == "y":
        christmasTrees()
    elif b == "n":
        c = input("Would you like to continue touring the Flee Market? (y or n): ")
        if c == "y":
            print("Alright, please confirm one more time and you will continue shortly...")
        elif c == "n":
            print("Thanks for shopping with us, bye!")
            exit()
        else:
            print("Please select a proper value next time, sending you back to Market...")
    else:
        print("Oh would you look at the time, it's time to close shop, see you next time!")
        exit()