# Hack 2
class factorial():
    def __init__(self,n):
        self.n = n

    def factorial(self,y=None):
        y = self.n if y is None else y
        product = 1
        for x in range(1,y+1):
            product*=x
        return product

    def __call__(self):
        series = [str(self.factorial(x)) for x in range(1,self.n+1)]
        return " ".join(series)


def dispfac():
    n = int(input("What factorial do you want? "))
    fac = factorial(n)
    print(fac.factorial())


def dispSeries():
    n = int(input("How long should the series be? "))
    fac = factorial(n)
    print(fac())

# Imperative Method
def superfac():
    x = int(input("What number should we use? "))
    product = 1
    for y in range(1,x+1):
        secondProd = 1
        for z in range(1,y+1):
            secondProd*= z
        product*=secondProd
    print(product)


class superFactorial():
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


# Imperative Method
def superfac():
    x = int(input("What number should we use? "))
    product = 1
    for y in range(1,x+1):
        secondProd = 1
        for z in range(1,y+1):
            secondProd *= z
        product *= secondProd
    print(product)


class palindrome():
    def __init__(self,string):
        self.string = string

    def __call__(self):
        testStr = self.string.lower()
        for x in [" ",",","-","."]:
            testStr = testStr.replace(x,"")
        if testStr == testStr[::-1]:
            return True
        else:
            return False
def printpal():
    string = input("Enter a word/sentence to test: ")
    pal = palindrome(string)
    if pal():
        print("That is a palindrome! ")
    else:
        print("Not a palindrome")
if __name__ == "__main__":
    dispSeries()