import re

def main():
    camelcase = input("camelCase: ")
    new = re.sub(r"([A-Z])", r"_\1", camelcase)
    new1 = re.sub(r"^_", "", new)
    print("snake_case: ", new1.lower())
    #for c in camelcase:
    #    re.sub(r"[A-Z]", "")
    #    print(c, end="")

main()
