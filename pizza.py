from tabulate import tabulate
import sys
import csv 

def main():
    if len(sys.argv) < 2:
        print("Too Few Command-line Argument!")
    elif len(sys.argv) > 2:
        print("Too Many Command-line Argument!")
    else:
        if sys.argv[1].endswith(".csv"):
            data = read_file(sys.argv[1])
            header = data[0]
            rows = data[1:]
            print(tabulate(rows, headers=header, tablefmt="grid" ))
        else:
            print("Not a csv File!")


def read_file(csv_file):
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        raise FileNotFoundError("File does not exit!")

if __name__ == "__main__":
    main()

