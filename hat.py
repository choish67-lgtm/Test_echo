import random

class Hat:
    houses = ["aa", "bb", "cc", "dd"]
#    def __init__(self):
#        self.houses = ["aa", "bb", "cc", "dd"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    #def sort(self, name):
    #    print(name, "is in", random.choices(self.houses, k=3))
    #    print(name, "is in", random.choice(self.houses))

Hat.sort("Harry")
#hat = Hat()
#hat.sort("Harry")