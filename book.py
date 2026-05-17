def main():
    with open("alice.txt", "r", encoding="utf-8") as f:
        contents = f.readlines()
#        contents = f.read()
    chapter1 = contents[52:272]
    print(chapter1[0])
    with open("chapter1.txt", "w", encoding="utf-8") as f:
#        f.write("Chater I.")
        f.writelines(chapter1)
main()