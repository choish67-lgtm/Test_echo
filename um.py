import re
import sys

def main():
    print(count(input("Test: ")))

def count(s):
    #word = re.split(r" +", s)
    word = s.split()
    #print(word)
    count_um = 0
    for i in word:
        clean_word = re.sub(r"[.+,+!+?+]", "", i)
        #print(clean_word)
        if re.fullmatch(r"um", clean_word):
            count_um += 1
    return count_um


if __name__ == "__main__":
    main()