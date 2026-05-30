import random

def main():
    level = get_level()
    problems = generate_integer(level)
    score = 0
    for n in range(5):
        i = 3        
        while i > 0:
            print(f"{problems[n][0]} + {problems[n][1]} = ", end="")
            answer = int(input())
            if (problems[n][0] + problems[n][1] == answer):
                score += 1
                break
            else:
                i -= 1
                if i > 0:
                    print("EEE")
                else:
                    right = problems[n][0] + problems[n][1]
                    print(f"{problems[n][0]} + {problems[n][1]} = {right}")
    print("Score: ", score)
                   
def get_level():
    while (level := int(input("Level: "))) not in [1, 2, 3]:
        pass
    return level

def generate_integer(digits):
    low = 10 ** (digits - 1)
    high = (10 ** digits) - 1
    pairs = [(random.randint(low, high), random.randint(low, high)) for _ in range(5)]
    return pairs

if __name__ == "__main__":
    main()
