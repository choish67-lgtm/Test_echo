def main():
    # miles = float(input("what's your miles? "))
    # minutes = float(input("what's your minutes? "))
    miles, minutes = map(float, input("what's your miles and minutes? ").split() )
    pace = get_pace(miles, minutes)
    print(f"You need to run each mile in {round(pace,3)}")
    numbers = list(map(float, input("Input 5 numbers. ").split()))
    print(numbers)

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0.")
    return minutes/miles

main()