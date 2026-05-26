"""
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

"""
# do the following at the terminal : "pip install mypy"
#def meow(n: int) -> None:    # type hint 
#    for _ in range(n):
#       print("meow")

def meow(n: int) -> str:    # type hint 
    """
    Meow n times.
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
print(meow,__doc__)
#meow(number)
#print("===============")


