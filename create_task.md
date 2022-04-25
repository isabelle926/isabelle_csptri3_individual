{% include nav.html %}

# Create Task Plan
## 3a. Provide a written response that does all three of the following:
_Approx. 150 words (for all subparts of 3a combined)_
### i. Describes the overall purpose of the program
The purpose of this program is to simulate how one would take care of a rat.
This project was born out of an interest to take care of pets as I have never had a pet before. 

### ii. Describes what functionality of the program is demonstrated in the video
The video demonstrates the user choosing a rat from several options, naming the rat, then interacting with the rat by feeding it, playing with it, and buying toys for it. 
The stats of the rat are shown after each option, and the game will end if the rat's health or the user's money is 0. 

### iii. Describes the input and output of the program demonstrated in the video
The user is able to input the type of rat and the name of the rat. The program will return these values when printing menu options, 
interacting with the various functions, and when the program prints the status of the rat. 
In addition, the user is also able to change the hunger and happiness values and the toys of the rat by using the functions listed in the main menu. 


## 3b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program. 
_Approx. 200 words (for all subparts of 3b combined, exclusive of program code)_
### i. The first program code segment must show how data have been stored in the list. 
```python
# rat dictionary
rat = {"name": "", "type": "", "age": 0, "hunger": 0, "health": 50, "happiness": 50, "toys": []}
```

### ii. The second program code segment must show the data in the same list being used , such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program's purpose. 
do later
```python
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


# purchase new toys
def buyToys():
    # define money as a global variable (again)
    global money
    print("Your " + rat["type"] + " " + rat["name"] + " deserves a treat for putting up with you! Let's get a new toy!")
    print("Here we have some toys that our researchers have chosen specifically for your breed of rat.")
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
```
### Then, provide a written response that does all three of the following:
### iii. Identifies the name of the list being used in this response
The name of the collection type is "rat". This is a dictionary. 

### iv. Describes what the data contained in the list represent in your program. 
The data contained in the list represents the values of the object that the user must interact with to play. 
It includes values that the user must maintain by interacting with the functions provided. 

### v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list.
The dictionary shown in the code segment is the most important collection type in my program as all other functions in my program revolves around interacting with these values. 
Without this list, I would have to create several variables and call them differently. 
For example, for the rat's name, I would have to create a variable the defines it as the input of the user, then I would have to define it as a global variable in every function that I used it in. 

## 3c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure.
_Approx. 200 words (for all subparts of 3c combined, exclusive of program code)_

### i. The first program code segment must be a student-developed procedure that:
- [ ] Defines the procedure's name and return type (if necessary)
- [ ] Contains and uses one or more parameters that have an effect on the functionality of the procedure
- [ ] Implements an algorithm that includes sequencing, selection, and iteration
```python
# purchase new toys
def buyToys():
    # define money as a global variable (again)
    global money
    print("Your " + rat["type"] + " " + rat["name"] + " deserves a treat for putting up with you! Let's get a new toy!")
    print("Here we have some toys that our researchers have chosen specifically for your breed of rat.")
    # ask users if they wish to proceed
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
```

### ii. The second program code segment must show where your student-developed procedure is being called in your program
```python
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
```

### Then, provide a written response that does both of the following:
### iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
The identified procedure allows the user to buy toys for their rat in exchange for money. 
In order to maintain the rat's happiness, the user must play with their rat, and they can only do so by purchasing the toys. 
By implementing this feature, users must be careful with their money and be smart when playing. 

### iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. 
First, the function declares money as a global variable so that it can be used within the function. 
Next, it prints some statements that inform the user as to what they are doing. 
It then uses a conditional to determine what will happen; if the user enters in 'y' or similar, then the function will print the toy options that correspond to the rat. 
It then asks the user it input a toy, and will add a toy to the rat["toy"] value. 
It will also subtract 100 from the money value. 
If the user says no, then the function merely returns the user to the main menu. 

## 3d. Provide a written response that does all three of the following:
_Approx. 200 words (for all subparts of 3d combined)_

### i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. 
### First call:
