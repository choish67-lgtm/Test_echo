def main():
    plate = input("Plate: ")
    if is_valid_2(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid_2(s):
    if not s or not 2 <= len(s) <= 6:
        return False
    
    i =0
    while i < len(s) and s[i].isalpha():
        i += 1
    letter_part = s[:i]
    digit_part = s[i:]
    if not letter_part:
        return False
    if digit_part and not digit_part.isdigit():
        return False
    if digit_part and digit_part[0] == "0":
        return False
    return True



def is_valid(s):
    middle = s[1:-1]
    conditions = [
        2 <= len(s) <= 6,
        not any(c.isdigit() for c in middle)
    ]

if __name__ == "__main__":
    main()
