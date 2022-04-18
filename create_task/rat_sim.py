# imports
import time

# rat dictionary
rat = {"name": "", "type": "", "age": 0, "hunger": 0, "health": 100, "happiness": 100, "toys": []}

# values that the user interacts with
money = 40


# pet toys
ratToys = {"brown rat": ["cardboard tube"], 
           "black rat": ["string"], 
           "grey rat": ["exercise wheel"], 
           "blue rat":["empty gatorade bottle"]}

# prompts user for different rats
def initRat():

  # type of rat
  ratType = ""

  ratOptions = list(ratToys.keys())
  print(ratOptions)

  while ratType not in ratOptions:
    