def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    #print(months.index("May"))
    input_data = input("Date: ")
    if "/" in input_data:
        date = input_data.split("/")
        print(f"{date[2]}-{date[0]}-{date[1]}")
    else:         
        date = input_data.split(" ")
        date[1] = date[1].replace(",", "")
        for i in months:
            if i.lower() == date[0].lower() :
                date[0] = months.index(i) + 1
                break
        print(f"{date[2]}-{date[0]}-{date[1]}")    

main()

"""  claude suggested as follows:
    if "/" in input_data:
        month, day, year = input_data.split("/")
    else:
        month, day, year = input_data.split(" ")
        day = day.replace(",", "")
        for i in months:
            if i.lower() == month.lower():   # 양쪽 모두 lower()
                month = months.index(i) + 1  # i를 그대로 사용
                break

    print(f"{year}-{int(month):02d}-{int(day):02d}")
"""