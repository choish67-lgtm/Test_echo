import random

def main():
    while True:
        number = int(input("Level: "))
        if number > 0:
            break

    gen_random = random.randint(1, number)

    while True:
        while (guess := int(input("Guess: "))) <= 0:
            pass
        #while True:
        #    guess = int(input("Guess: "))
        #    if guess > 0:
        #        break            
        if guess > gen_random:
            print("Too Large!")
        elif guess < gen_random:
            print("Too Small!")
        else:
            print("Just Right!")
            break

main()

"""
while (guess := int(input("Guess: "))) <= 0:
    pass
"""

"""
def get_positive():
    while True:
        n = int(input("Guess: "))
        if n > 0:
            return n

guess = get_positive()
"""