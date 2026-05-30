def main():
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


        
