# test3
"""
print("While Loop\n")
i = 0
while i < 3:
    print("meow")
    i += 1

print("\nFor Loop")
# for i in [0, 1, 2]:
# for i in range(5):
for _ in range(5):
    print("meow")

print("3\n")
print("meow\n" * 3, end="")

while True:
    n = int(input("what's n? "))
    if n < 0:
        continue
    else:
        break

while True:
    n = int(input("what's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()



students = ["Hermione", "Harry", "Ron"]
# for student in students:
#     print(student)
for i in range(len(students)):
    print(i+1, students[i])

# LIST
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron":  "Gryffindor",
    "Draco": "Slytherin",
    }
for student in students:
    print(student, students[student], sep=", ")
print(students["Ron"])

# DICT
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jact Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for student in students:
#    print(student)
    print(student["name"], student["house"], student["patronus"],sep=", ")

def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")
#    for _ in range(height):
#        print("#")

main()


def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
"""

def main():
    print_square_1(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

def print_square_1(size):
    for i in range(size):
        print("#" * size)
        print_row(size)

def print_row(width):
    print("#" * width)

main()