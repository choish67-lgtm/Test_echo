import re

def main():
    print(shorten(input("Input: ")))
    
def shorten(word):
    return re.sub(r"[AEIOUaeiou]", "", word)
    #output_str = re.sub(r"[AEIOUaeiou]", "", word)
    #return output_str

if __name__ == "__main__":
    main()