{% include nav.html %}
## Tech Talk 0: Python Menu, Replit, Github

For this challenge, I decided to make a menu in the style of a text adventure.

I constructed my menu by using dictionaries:

Main menu:
```python
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
    4: {"display":"Polly's Penguins",
        "exec":InfoDb,
        "type":"dict"},
    5: {"display":"Fred's Fun Math and More",
        "exec":Math,
        "type":"dict"},
    6: {"display":"Quit Program",
        "exec":quit,
        "type":"func"}
}
```
Submenus:
```python
InfoDb = {
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
        "display":"Return to Market",
        "exec": market,
        "type":"func"
    },
    5: {
        "display":"Quit program",
        "exec": quit,
        "type":"func"
    },
}

Math = {
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
        "display":"Fibonacci",
        "exec": fibonacci,
        "type":"func"
    },
    6: {
        "display":"Return to Market",
        "exec": market,
        "type":"func"
    },
    7: {
        "display":"Quit program",
        "exec": goodbye,
        "type":"func"
    },
}
```

Functions that build and present the menu:
```python
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
```
Christmas tree + keypad code: 
```python
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
```
Animations:
```python
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
```
Final replit runtime:
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@IsabelleGunawa1/isabellecsptri3individual?embed=true"></iframe>
