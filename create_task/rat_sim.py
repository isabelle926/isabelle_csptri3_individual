# imports
import time

# rat dictionary
rat = {"name": "", "type": "", "age": 0, "hunger": 0, "health": 50, "happiness": 50, "toys": []}

# values that the user interacts with
money = 30

# rat toys
ratToys = {"brown rat": ["cardboard tube", "hammock", "plastic bag"],
           "black rat": ["string", "rawhide", "red bean bag"],
           "grey rat": ["exercise wheel", "apple stick", "toilet paper"],
           "blue rat": ["empty gatorade bottle", "dollhouse", "soda can box maze"]}


# prompts user for different rats
def initSim():
    # type of rat
    ratType = ""
    ratOptions = list(ratToys.keys())

    while ratType not in ratOptions:
        print("Welcome to Randy's rat store! We have lots of rats here: ")
        for option in ratOptions:
            print(option)
        ratType = input("Which one would you like?")

    # add rat type to rat dictionary
    rat["type"] = ratType

    # name the rat
    rat["name"] = input("What would you like to name your " + rat["type"] + "?")


# print menu
def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Interact with the rat: ")
    for key in optionKeys:
        print(key + ":\t" + menuOptions[key]["desc"])


# feed the rat
def feedRat():
    # define money as a global variable so it can be used within functions
    global money
    if rat["hunger"] <= 0:
        print("Your rat is already full! Returning to menu")
    else:
        choice = input(
            "Would you like to spend 15 dollars to feed your rat? You have " + str(money) + " dollars. (y/n) ")
        # define money as a global variable so that it can be used inside functions
        if choice == "yes" or "y":
            money -= 15
            rat["hunger"] -= 30
            print("Fed your rat! Hunger has decreased by 30. ")
        else:
            print("Returning to menu")


# play with toys
def play():
    if len(rat["toys"]) == 0:
      buyChoice = input("You have no toys. Would you like to buy some? (y/n) ")
      if buyChoice == "y" or "yes" or "Y" or "Yes":
        buyToys()
      else:
        print("Seeya later.")
    else:
        print("Here are the toys you have: ")
        toyChoice = ""
        while toyChoice not in rat["toys"]:
            for toy in rat["toys"]:
                print(toy)
            toyChoice = input("Which toy would you like to play with? ")
        rat["happiness"] += 30
        print(rat["name"] + " had a great time playing with the " + toyChoice + "! Increased happiness by 30.")


# purchase new toys
def buyToys():
    # define money as a global variable (again)
    global money
    print("Your " + rat["type"] + " " + rat["name"] + " deserves a treat for putting up with you! Let's get a new toy!")
    print("Here we have some toys that our researchers have chosen specifically for your breed of rat.")
    # ask users if they wish to continue
    moneyChoice = input("By the way, toys cost 100 dollars each. Do you still want to buy one? (y/n)")
    if moneyChoice == "yes" or "y" or "Y":
        print("Alright, here are your choices: ")
        toyOption = ratToys[rat["type"]]
        print(toyOption)

        # user choice
        toyNum = -1

        # ask user for toy choice
        while toyNum < 0 or toyNum > len(toyOption) - 1:
            for i in range(len(toyOption)):
                print(str(i) + ": " + toyOption[i])
            toyNum = int(input("Please select the number of the toy you would like: "))

        # add chosen toy to rat toys
        chosenToy = toyOption[toyNum]
        rat["toys"].append(chosenToy)
        money -= 100
        print("Good choice. I think " + rat["name"] + " will enjoy playing with the " + chosenToy)
    else:
        print("Goodbye cheapskate.")


# print status of the rat
def printStatus():
    # once again, money needs to be a global variable
    global money

    # conditional statements that print different statements using AND operators
    if rat["hunger"] < 50 and rat["health"] > 50 and rat["happiness"] > 50:
        print("Your " + rat["type"] + " " + rat["name"] + " is doing great!")
    else:
        print("Uh oh, your " + rat["type"] +" " + rat["name"] + " isn't doing so well.")
    time.sleep(1)
    print("Your rat currently has: " + str(len(rat["toys"])) + " toys, which are: ")
    for toy in rat["toys"]:
        print(toy)
    time.sleep(1)
    print("Your pet currently has a hunger level of " + str(rat["hunger"]) + ".")
    time.sleep(1)
    print("Your pet currently has a health level of " + str(rat["health"]) + ".")
    time.sleep(1)
    print("Your pet currently has a happiness level of " + str(rat["happiness"]) + ".")
    time.sleep(1)
    print("Your pet is " + str(rat["age"]) + " days old.")
    time.sleep(1)
    print("You have " + str(money) + " dollars")
    time.sleep(1)


# main
def main():
    # don't forget to make sure money is a global variable!
    global money
    # start game
    initSim()

    menuOptions = {
        "F": {"func": feedRat,
              "desc": "Feed " + rat["name"]},
        "P": {"func": play,
              "desc": "Play with " + rat["name"]},
        "B": {"func": buyToys,
              "desc": "Buy toys for " + rat["name"]},
        "Q": {"func": quit,
              "desc": "Quit Program"}
    }

    keepPlaying = True
    while keepPlaying:
        menuSelection = ""
        while menuSelection not in menuOptions:
            printMenu(menuOptions)
            menuSelection = input("What would you like to do? ").upper()

        # runs the chosen function
        menuOptions[menuSelection]["func"]()

        # increases rat stats
        rat["hunger"] += 10
        rat["age"] += 1
        rat["happiness"] -= 10

        # increases user money
        money += 70

        # more conditionals
        if rat["hunger"] > 40 or rat["happiness"] < 40:
            rat["health"] -= 10
        elif rat["hunger"] < 30 and rat["happiness"] > 50:
            rat["health"] += 10

        # conditionals that will end the game
        if money == 0:
            print("You are broke! Your rat has left you for someone richer. ")
            quit()
        elif rat["health"] <= 0:
            print("Your rat has died! Maybe try taking care of a plant first.")
            quit()

        printStatus()
        print()


if __name__ == "__main__":
    main()
