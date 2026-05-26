import re

locations = {"+1": "USA and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        #country_code = match.group(1)
        country_code = match.group("country_code")
        print("Country code is ", country_code)
        print(locations[country_code])
    else:
        print("Invalid")

main()