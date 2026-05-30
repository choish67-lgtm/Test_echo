import sys
import csv

def main():
    if len(sys.argv) < 3:
        print("Too Few Command-line Argument!!")
    elif len(sys.argv) > 3:
        print("Too Many Command-line Argument!!")
    else:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            data, fieldnames = read_file(sys.argv[1])
            new_rows = []
            for row in data:
                last, first = row["name"].split(", ")
                new_row = {
                    "first_name": first,
                    "last_name": last,
                    "house": row["house"]
                }
                new_rows.append(new_row)
            new_fieldnames = list(new_rows[0].keys())
            write_file(sys.argv[2], new_rows, new_fieldnames)

        else:
            print("Can't Find csv Files!")

def read_file(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader), list(reader.fieldnames)
            #fieldnames = reader.fieldnames
            #data = list(reader)
            #return data, fieldnames
    except FileNotFoundError:
        raise FileNotFoundError("csv reader file does not exist!!")

def write_file(file, data, fieldnames):
    with open(file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
if __name__ == "__main__":
    main()
