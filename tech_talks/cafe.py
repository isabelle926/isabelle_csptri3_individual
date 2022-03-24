from time import sleep
def coolCafe():
    print("Welcome to Cathy's Café!")
    for key in cafemenu_options.keys():
        print(key, '--', cafemenu_options[key])
    runCafeOptions()


cafemenu_options = {
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


def runCafeOptions():
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