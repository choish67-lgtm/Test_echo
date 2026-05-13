"""
import random
coin = random.choice(["heads", "tails"])

# from random import choice
# coin = choice(["heads", "tails"])

print(coin)

number = random.randint(-100, 100)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)


import statistics
print(statistics.mean([100, 90]))
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments======")
    print(sys.arg)

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
    print(sys.argv)

"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
#else:
#    print("hello, my name is", sys.argv[1])
print("hello, my name is", sys.argv[1])

   
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
    """

 