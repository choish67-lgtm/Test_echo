from datetime import date, datetime

#class FutureDateError(Exception):
#    pass

def main():
    birth_str = input("Date of Birth: ")
    try:
        days, hours, minutes, seconds = cal_days(birth_str)
        print(f"{days:,} days")
        print(f"{hours:,} hours")
        print(f"{minutes:,} minutes")
        print(f"{seconds:,} seconds")
    except ValueError as e:
        if "later" in str(e):
            print("Birthday is later than Today!")
        else:
            print("Invalid Date Format!")
    #except FutureDateError:
    #    print("Birthday is later than Today!")

def cal_days(birth_str):
    #birthday = datetime.strptime(birth_str, "%Y-%m-%d").date()
    birthday = datetime.fromisoformat(birth_str).date()
    today = date.today()
    if birthday > today:
        #raise FutureDateError("Birthday is later than Today!")
        raise ValueError("Birthday is later than Today!")

    diff = today - birthday

    total_days    = diff.days
    total_seconds = diff.total_seconds()
    total_minutes = total_seconds / 60
    total_hours   = total_seconds / 3600
    return int(total_days), int(total_hours), int(total_minutes), int(total_seconds)

if __name__ == "__main__":
    main()