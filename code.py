import re

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[0-9A-Fa-f]{6}$"
    if match := re.search(pattern, code, re.IGNORECASE):
        print(f"Valid. Matched with {match.group()}")
"""
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")
"""
main()