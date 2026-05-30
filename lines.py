import sys
import re

def main():
    if len(sys.argv) < 2:
        sys.exit("Too Few Command-line Argument")
    elif len(sys.argv) > 2:
        sys.exit("Too Many Command-line Argument")
    
    input_file = sys.argv[1]

    if ".py" in input_file: # if sys.argv[1].endswith(".py")
        file_contents = read_file(input_file)          
        n = 0
        for line in file_contents:
            #if line.startswith("#"):
            if re.match(r"^( )*#", line):
                pass
            elif line == "\n":
                pass
            else:
                n += 1
        print(n)
    else:
        sys.exit("Not a Python file")


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist!")
    
if __name__ == "__main__":
    main()