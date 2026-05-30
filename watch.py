import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    contents = s.split(" ")
    output_address = []
    for i in contents:
        if re.search("src=", i):
            address_1 = re.sub(r"src=\"", "", i)
            output_address = re.sub(r"\".*", "", address_1)
    return output_address
        

if __name__ == "__main__":
    main()

