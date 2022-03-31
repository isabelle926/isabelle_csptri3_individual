# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

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
# List with dictionary records placed in a list

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Species"], InfoDb[n]["Scientific Name"])  # using comma puts space between values
    print("\t", "Fun Facts: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Fun Facts"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for x in InfoDb:
        for key,value in x.items():
            print(f"{key}: {value}")
        print()
        print("-"*10)
        print()


## hack 2b: def while_loop(0)
def while_loop():
    x = 0
    while x < len(InfoDb):
        for key,value in InfoDb[x].items():
            print(f"{key}:{value}")
        print()
        print('-'*10)
        print()
        x += 1


## hack 2c : def recursive_loop(0)
def recursive_loop():
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


# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
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

