class Package:
    def __init__(self, number=0, sender="", recipient="", weight=0):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Information! \nPackage {self.number}: {self.sender} to {self.recipient}, weight={self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=3, sender="Bob", recipient="Charlie", weight=5)
    ]
#    packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    print(packages)
    print("==========")
    for package in packages:
    #    print(package.number)
    #    print(f"Package {package.number}")
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")
        print("==========")

main()
package10 = Package(10, "choi", "park", 100)
print(package10)
print(f"{package10} costs ${package10.calculate_cost(cost_per_kg=5)}")