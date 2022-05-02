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
    # ask users if they wish to continue
    moneyChoice = input("By the way, toys cost 100 dollars each. Do you still want to buy one? (y/n)")

    if moneyChoice.lower() == "n":
        print("Goodbye. ")
    else:
        # if moneyChoice == "yes" or "y" or "Y":
        print("Alright, here are your choices: ")
        toyOption = ratToys[rat["type"]]

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
        playChoice = input("Would you like to play with the toy now? (y/n) ")
        if playChoice == "y" or "Y" or "yes" or "Yes":
            playToy(chosenToy)
            time.sleep(1)
        else:
            print("Goodbye. ")
    # else:
    # print("Goodbye cheapskate.")
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
- [x] Defines the procedure's name and return type (if necessary)
- [x] Contains and uses one or more parameters that have an effect on the functionality of the procedure
- [x] Implements an algorithm that includes sequencing, selection, and iteration

```python
def playToy(toy):
    if toy.lower() == "hammock" or "rawhide" or "apple stick" or "dollhouse":
        print("Let's play with your rat! ")
        rps_list = ["rock", "paper", "scissors"]
        rat_choice = rand.choice(rps_list)
        rpsChoice = ""
        while rpsChoice not in rps_list:
            rpsChoice = input("Choose rock, paper, or scissors: ").lower()
        print("You chose " + rpsChoice + ", " + rat["name"] + " chose " + rat_choice)
        if rpsChoice == rat_choice:
            print("You both selected " + rpsChoice + ". It's a tie!")
        elif rpsChoice == "rock":
            if rat_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif rpsChoice == "paper":
            if rat_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif rpsChoice == "scissors":
            if rat_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

    elif toy.lower() == "cardboard tube" or "string" or "exercise wheel" or "empty gatorade bottle":
        print("Your rat feels like exercising. Let's play a game while we wait! ")
        randomnum = rand.randint(1, 100)
        print("Guess a number between 1 and 100")
        while True:
            guess = int(input())
            if guess < randomnum:
                print("Too low")
            elif guess > randomnum:
                print("Too high")
            else:
                print("That's right!")
                break
    else:
        print("Your rat wants to go on an adventure: ")
        place = input("Enter a place: ")
        noun = input("Enter a plural noun: ")
        food = input("Enter a food: ")
        verb = input("Enter a verb ending in 'ing': ")
        print("One day, " + rat[
            "name"] + " ventured off to " + place + " to search for some " + noun + ". However, after " + verb + " for so long, " +
              rat["name"] + " became tired and started eating some " + food)
```

### ii. The second program code segment must show where your student-developed procedure is being called in your program
```python
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
        playToy(toyChoice)
        time.sleep(1)
        rat["happiness"] += 30
        print(rat["name"] + " had a great time playing with the " + toyChoice + "! Increased happiness by 30.")
```

### Then, provide a written response that does both of the following:
### iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
The identified procedure allows the user to play minigames depending on what toy they choose to use. 
This allows for more engagement with the game and makes it more "fun." 
The "sequencing" is the order in which each line is executed so that the program is sensible and usable, the "selection" is the program that is played based on user choice, and the "iteration" is the while loop that plays until the user makes a choice. 

### iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. 
First, the procedure asks the user to choose a toy to play with. Depending on what rat the user initially chose, they will have different options. 
However, each type has three unique toys that allow for different minigames to be played.
The first 'if' statement prompts the user to guess a number. The second conditional, the 'elif' statement allows the user to play rock, paper, scissors. 
The final conditional allows the user to play a Madlibs game and create their own story. 

## 3d. Provide a written response that does all three of the following:
_Approx. 200 words (for all subparts of 3d combined)_

### i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. 
### First call:
```python
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
        playToy(toyChoice)
        time.sleep(1)
        rat["happiness"] += 30
        print(rat["name"] + " had a great time playing with the " + toyChoice + "! Increased happiness by 30.")
```
### Second call:
```python
# purchase new toys
def buyToys():
    # define money as a global variable (again)
    global money
    print("Your " + rat["type"] + " " + rat["name"] + " deserves a treat for putting up with you! Let's get a new toy!")
    print("Here we have some toys that our researchers have chosen specifically for your breed of rat.")
    # ask users if they wish to continue
    moneyChoice = input("By the way, toys cost 100 dollars each. Do you still want to buy one? (y/n)")

    if moneyChoice.lower() == "n":
        print("Goodbye. ")
    else:
        # if moneyChoice == "yes" or "y" or "Y":
        print("Alright, here are your choices: ")
        toyOption = ratToys[rat["type"]]

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
        playChoice = input("Would you like to play with the toy now? (y/n) ")
        if playChoice == "y" or "Y" or "yes" or "Yes":
            playToy(chosenToy)
            time.sleep(1)
        else:
            print("Goodbye. ")
    # else:
    # print("Goodbye cheapskate.")
```

### ii. Describes what condition(s) is being tested by each call to the procedure
### Condition(s) tested by the first call:
The first call occurs when the user chooses the menu option to play with their rat. 
Upon choosing what toy to play with, the playToy function uses that input in order to pass it through the procedure.

### Condition(s) tested by the second call:
The second call occurs after a user has bought a toy for their rat to play with. 
After buying the toy, the user is prompted as to whether or not they would like to play with it. 
If the user answers "yes", then the playToy function will pass the toy they just bought into the procedure.

### iii. Identifies the result of each call
### Result of the first call:
The minigame that is shown is dependent on what the user selected when choosing a toy to play with. 
For example, if they have a brown rat and chose to play with a cardboard tube, then the minigame that appears will be a guess the number game. 

### Result of the second call:
The playToy function shows a different minigame depending on what toy the user bought. 
For example, if they have a blue rat and chose to play with the dollhouse, then the user will be prompted to play a game of rock, paper, scissors. 


