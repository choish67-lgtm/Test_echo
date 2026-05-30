import re

def main():
    file_name = input("Enter your file name: ").strip()
    print(media_types(file_name))

def media_types(fn):
    f_name, f_extension = fn.split(".")
    if re.match(r"gif", f_extension):
        return ("image/gif")
    elif re.match(r"jp[e]*g", f_extension):
        return ("image/jpeg")
    else:
        return ("application/octet-stream")
    
main()
    
