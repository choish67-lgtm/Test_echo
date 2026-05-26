def main():
    #yell(["This", "is", "CS50"])
    yell1("This", "is", "CS50")

def yell1(*words):
    #uppercased = map(str.upper, words)
    uppercased = [word.upper() for word in words]
    print(*uppercased)

numbers = [1, 2, -3]
squares = map(lambda x: x*x, numbers)
print(list(squares))

abstract = map(lambda x: abs(x), numbers)
print(list(abstract))
print("==========")

t1 = [1, 2, 4, 0, -2]
print("length of t1:", len(t1))
print(t1)
t1.append(100)
print("length of t1_append:", len(t1))
print(t1)
t1.sort()
print(t1)
t1.reverse()
print(t1)
t1.remove(100)
print(t1)
t1.extend([1, 100, 200])
print(t1)
t1.append([1, 100, 200])
print(t1)
print("==========")

t2 = (1, 3, 6, 4)
print("length of t2:", len(t2))

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    print(uppercased)

if __name__ == "__main__":
    main()