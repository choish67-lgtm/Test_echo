import re

def main():
    math_problem = input("Expression: ").strip()
    print(math_cal(math_problem))
    
def math_cal(n):
    x, y, z = re.split(r"[ ]+", n)
    if y == "+":
        return f"{int(x) + int(z):,.1f}"
    elif y == "-":
        return f"{int(x) - int(z):,.1f}"
    elif y == "*":
        return f"{int(x) * int(z): ,.1f}"
    elif y == "/" and int(z) != 0:
        return f"{int(x)/int(z):,.1f}"
    else:
        return f"""
        =========  Result  =========
        Invalid Expression
        ============================
        """
        #return "Invalid Expression"
    
main()