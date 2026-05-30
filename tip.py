def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    print(d)
    dollars_float = d.removeprefix('$')
    dollars, cents = dollars_float.split('.')
    return int(dollars)

def percent_to_float(p):
    print(p)
    percent_float = p.removeprefix('%')
    tip_percent, tip_percent_float = percent_float.split('.')
    return int(tip_percent)/100

main()