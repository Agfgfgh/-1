# Define a dictionary to store the animals
animals_data = {
    "Dog12": "Dog",
    "CAT3": "Cat",
    "LiOn7": "Lion",
    "DolphiN11": "Dolphin",
    "fish6": "Fish",
    "PIG17": "Pig",
    "bear29": "Bear",
    "BiRd8": "Bird",
    "SNAKE39": "Snake",
    "donkey14": "Donkey"
}
def search_by_code():
    code = input("הכנס קוד חיה: ")
    if code in animals_data:
        print(f"קוד חיה: {code}\nשם החיה: {animals_data[code]}")
    else:
        print("לא נימצא נסה שוב")

def search_by_name():
    name = input("הכנס שם החיה: ")
    results = [animal for animal in animals_data.items() if name.lower() in animal[1].lower()]
    if results:
        for code, name in results:
            print(f"קוד חיה: {code}\nשם החיה: {name}")
    else:
        print("לא נימצא נסה שוב")

def add_animal():
    code = input("הכנס קוד חיה: ")
    if code in animals_data:
        print("לא ניתן ניתן להוסיף החיה נמצאת במאגר")
    else:
        name = input("הכנס שם החיה: ")
        animals_data[code] = name
        print("החיה נוספה בהצלחה")

def remove_animal():
    code = input("הכנס קוד חיה: ")
    if code not in animals_data:
        print("לא נימצא נסה שוב")
    else:
        del animals_data[code]
        print("החיה הוסרה בהצלחה")

def print_menu():
    print("""
" ברוכים הבאים למאגר מידע של גן החיות ,
אנא בחר אפשרות:
[1 – ]חיפוש חיה ע"י קוד 
[2 – ]חיפוש חיה ע"י שם  
    [3 – ]הוספת חיה חדשה
[4 – ]מחיקת חיה מהמאגר  
[5 – ]יציאה             
""")

def main():
    while True:
        print_menu()
        choice = int(input("הכנס את בחירתך: "))
        if choice == 1:
            code = input("הכנס קוד החיה: ")
            if code in animals_data:
                print(f"קוד חיה: {code}\nשם החיה: {animals_data[code]}")
            else:
                print("לא נימצא נסה שוב")
        elif choice == 2:
            search_by_name()
        elif choice == 3:
            add_animal()
        elif choice == 4:
            remove_animal()
        elif choice == 5:
            print("להיתראות")
            break
        else:
            print("לא נימצא נסה שוב.")

if __name__ == "__main__":
    main()
