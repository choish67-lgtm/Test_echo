def main():
    face = input("what's your smile? ")
    print(convert(face))


def convert(face):
    if face == ":)":
        return "😊"
    elif face == ":(":
        return "😒"
    else:
        return face

if __name__ == "__main__":
    main()
