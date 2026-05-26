class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["aa", "bb", "cc", "dd"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "👌"
            case "Otter":
                return "😂"
            case "Jack":
                return "🤣"
            case _:
                return "/"

def main():
    #name, house = get_student()
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
#    if student["name"] == "Padma":
#        student["house"] = "Ravenclaw"
#    print(f"student['name'] from student['house'])
#    print(f"{student.name} from {student.house}")

    #name = get_name()
    #house = get_house()
    #print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
#    try:
#       return Student(name, house)
#    except ValueError:
    

#    return Student(name, house)
#    student = Student(name, house)
#    return student
"""   
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
"""
#    name = input("Name: ")
#    house = input("House: ")
#    return {"name": name, "house": house}
#    student = {}
#    student["name"] = input("Name: ")
#    student["house"] = input("House: ")
#    return student

"""
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)    # tuple is immutable
    #return [name, house]   # list is mutable
"""
if __name__ == "__main__":
    main()