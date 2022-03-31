## Tech Talk 1: Data Structures
### Hack 1: Python lists
```python
InfoDb = [{
    "Species": "African black-footed penguin",
    "Conservation Status": "Endangered",
    "Scientific Name": "Spheniscus demersus",
    "Location": ["South Africa", "Namibia"],
    "Family": "Spheniscidae",
    "Fun Facts": ["Only penguins in Africa", "Around 2 ft tall", "Eats fish, squid, crustaceans"]
}, {
    "Species": "Northern rockhopper penguin",
    "Conservation Status": "Endangered",
    "Scientific Name": "Eudyptes moseleyi",
    "Location": ["Tristan da Cunha", "Gough Island"],
    "Family": "Spheniscidae",
    "Fun Facts": ["One of the smallest crested penguin", "Around 5 lbs", "Are scrappy and pugnacious"]
}, {
    "Species": "King penguin",
    "Conservation Status": "Least Concern",
    "Scientific Name": "Aptenodytes patagonicus",
    "Location": ["Falkland Islands"],
    "Family": "Spheniscidae",
    "Fun Facts": ["Fuzzy brown chicks", "Look similar to emperor penguins", "Around 3 ft tall"]
}, {
    "Species": "Adélie penguin",
    "Conservation Status": "Near Threatened",
    "Scientific Name": "Pygoscelis adeliae",
    "Location": ["Antartica"],
    "Family": "Spheniscidae",
    "Fun Facts": ["Attack with their flippers", "Characteristic 'tuxedo' look", "Smallest penguin in Antarctica"]
}]
```
### Hack 2: Loops
For loops:
```python
def for_loop():
    print("Welcome, meet our penguins!")
    print()
    print("-"*10)
    print()
    for x in InfoDb:
        for key,value in x.items():
            print(f"{key}: {value}")
        print()
        print("-"*10)
        print()
```
While loops:
```python
def while_loop():
    print("Welcome, meet our penguins!")
    print()
    print("-"*10)
    print()
    x = 0
    while x < len(InfoDb):
        for key,value in InfoDb[x].items():
            print(f"{key}:{value}")
        print()
        print('-'*10)
        print()
        x += 1
```
Recursive loops:
```python
def recursive_loop():
    print("Welcome, meet our penguins!")
    print()
    print("-"*10)
    print()
    n = 0
    if n >= len(InfoDb):
        return
    else:
        for key, value in InfoDb[n].items():
            print(f"{key}:{value}")
        print()
        print("-"*10)
        print()
        if n == 0:
            y = n + 1
            for key, value in InfoDb[y].items():
                print(f"{key}:{value}")
            print()
            print("-"*10)
            print()
            if y == 1:
                z = y + 1
                for key, value in InfoDb[z].items():
                    print(f"{key}:{value}")
                print()
                print("-"*10)
                print()
```
### Hack 3: Fibonacci
```python
def fibonacci():
    # Program to display the Fibonacci sequence up to n-th term
    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    try:
        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")

        # if there is only one term, return n1
        elif nterms == 1:
            print("Fibonacci sequence up to",nterms,":")
            print(n1)

        # generate fibonacci sequence
        else:
            print("Fibonacci sequence:")
            while count < nterms:
                print(n1)
                nth = n1 + n2

                # update values
                n1 = n2
                n2 = nth
                count += 1
    except:
        print("sorry error")
```