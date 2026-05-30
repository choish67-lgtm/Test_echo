import sys
import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(input_address):
    IP_address = input_address.split(".")
    if len(IP_address) != 4:
        return False    
    for i in IP_address:
        if not i.isdigit():
            return False
        if not (0 <= int(i) <= 255):
            return False
    return True


if __name__ == "__main__":
    main()
