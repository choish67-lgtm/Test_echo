import validators

def main():
    print(is_valid_email(input("what's your email address? ")))

def is_valid_email(s):
    result = validators.email(s)
    #print(result)
    #print(type(result))
    return bool(result)


main()