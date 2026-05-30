def main():
    fruit_nutrition = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "kiwi": "90"
    }

    fruit = input("Item: ")
   
    if fruit in fruit_nutrition:
        print("Calories: ", fruit_nutrition[fruit])
    else:
        print("")
    
main()
