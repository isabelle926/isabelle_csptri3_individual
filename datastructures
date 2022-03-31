## Key Learnings

### Tech Talk 0:
```python
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
Isabelle learned things

add more code blocks here later

### Tech Talk 1:
```pythondef fibonacci():
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
Isabelle learned more things

### Tech Talk 2:
```pythonclass superFactorial():
    def __init__(self,n):
        self.n = n

    def factorial(self,y):
        y = self.n if y is None else y
        product = 1
        for x in range(1,y+1):
            product *= x
        return product

    def __call__(self):
        product = 1
        for x in range(1,self.n+1):
            product *= self.factorial(x)
        return product

```
Isabelle learned even more things!!!
