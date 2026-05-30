import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(input_hours):
    hours = input_hours.split(" ")

    if ":" not in hours[0]:
        hours[0] += ":00"
    if ":" not in hours[3]:
        hours[3] += ":00"

    new_hour_0, new_min_0 = hours[0].split(":")
    new_hour_3, new_min_3 = hours[3].split(":")

    new_hour_0 = int(new_hour_0)
    new_hour_3 = int(new_hour_3)

    if hours[1].upper() == "PM" and new_hour_0 != 12:
        new_hour_0 += 12
    if hours[1].upper() == "AM" and new_hour_0 == 12:
        new_hour_0 = 0

    if re.search(r"(?i)PM", hours[4]) and new_hour_3 != 12:
        new_hour_3 += 12
    if re.search(r"(?i)AM", hours[4]) and new_hour_3 == 12:
        new_hour_3 = 0    

    return f"{int(new_hour_0):02}:{new_min_0} to {int(new_hour_3):02}:{new_min_3}"


if __name__ == "__main__":
    main()




