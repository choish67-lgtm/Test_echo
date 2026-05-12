# test2

"""
x = int(input("what's x? "))
y = int(input("what's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


score = int(input("Score: "))

#if score >= 90 and score <= 100:
if 90 <= score <= 100:
    print("Grade: A")
elif score >= 80 and score <80:
    print("Grade: B")
else:
    print("Grade: C")

def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0
#    return True if n % 2 == 0 else False
#   if n % 2 == 0:
#      return True
#   else:
#      return False
   
main()

"""
name = input("what's your name? ")

match name:
    case "Harry" | "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
        
"""
if name == "Harry" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

