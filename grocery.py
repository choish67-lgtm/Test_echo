def main():
    try:
        grocery = {}
        while True:
            item = input()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
    except EOFError:
        for item, count in grocery.items():
            if item != "":
                print(f"{count} {item.upper()}") 
        #    break

main()           
