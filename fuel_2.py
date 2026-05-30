def main():
    try:
        final_result = gauge(convert(input("Fraction: ")))
    except ValueError as e:
        final_result = e
    except ZeroDivisionError as e:
        final_result = e

    print(final_result)

    #print(gauge(convert(input("Fraction: "))))    

def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if x < 0 or y < 0:
        raise ValueError("Negative Number Not Allowed!")
    elif y == 0:
        raise ZeroDivisionError("Zero Divider Not Allowed!")
    else:
        return float(x/y)

def gauge(percentage):
    percent = round(percentage * 100)
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()

"""
    try:
        x, y = map(int, input("Fraction: ").split("/"))

        if x < 0 or y < 0:
            raise ValueError(f"Both {x} and {y} should be Greater than 0.")
        if y == 0:
            raise ZeroDivisionError(f"{y} must not be zero.")         
        
        result = round(float(x/y) * 100) 

        if result <= 1:
            print("E")
        elif result >= 99:
            print("F") 
        else:    
            print(f"{result}%")
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")


main()

"""
        
