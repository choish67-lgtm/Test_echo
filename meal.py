def main():
    time = input("what time is it? ")
    if (convert(time) >= 7.0 and convert(time) <= 8.0):
        print("breakfast time")
    elif (convert(time) >= 12.0 and convert(time) <= 13.0):
        print("lunch time")
    elif (convert(time) >= 18.0 and convert(time) <= 19.0):
        print("dinner time")
    else:
        print("")

def convert(time):
    hour, minute = time.split(":")
    return float(int(hour) + int(minute)/60)

if __name__ == "__main__":
    main()