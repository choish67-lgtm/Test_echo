
with open("students.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
    print("======")
"""
students =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
print("======")

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")



with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["home"]):
    print(f"{student['name']} is in {student['home']}")
    print(student)


with open("students.csv") as file:
    reader = csv.reader(file)
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        #student = {}
        #student["name"] = name
        #student["house"] = house
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

#for student in sorted(students, key=get_name, reverse=False):
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student['house']}")

"""


import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("students1.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

with open("students2.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writeheader()
    writer.writerow({"name": name, "home": home})
