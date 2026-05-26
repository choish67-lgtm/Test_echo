import sys

if len(sys.argv) == 1:
    print("MEOW")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("MEOW")
else:
    print("usage: meow.py")