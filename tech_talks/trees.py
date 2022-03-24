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
    print("Thanks for shopping with us, bye!")
    exit()