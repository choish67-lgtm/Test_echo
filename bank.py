import re

balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

# Homework
greeting = input("Greeting: ").lstrip()
print(greeting)
if re.match(r"[hH]ello[, ]*", greeting):
    print("$0")
    print(re.match(r"[hH]ello[, ]*", greeting).group())
elif re.match(r"[hH]", greeting):
    print("$20")
    print(re.match(r"[hH]", greeting).group())
else:
    print("$100")


    
if __name__ == "__main__":
    main()


