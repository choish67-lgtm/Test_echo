def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)
    print("======")
    #for i in range(n):
    #    #print("🐏" * i)
    #    print(sheep(i))

def sheep(n):
    #return "🐏" * n
    #flock = []
    #for i in range(n):
    #    flock.append("🐏" * i)
    #return flock
    for i in range(n):
        yield "🐏" * i


if __name__ == "__main__":
    main()