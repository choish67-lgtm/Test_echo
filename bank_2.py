import re

def main():
    greeting = input("Greeting: ").lstrip()
    print(value(greeting))

def value(greeting):
    if re.match(r"[hH]ello[, ]*", greeting):
        return "$0"
    elif re.match(r"[hH].+", greeting):
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()


