

def check_data_in_dict():
    
    data_list = [
        {"name": "hager", "age": 24, "city": "doha"},
        {"name": "sara", "age": 21, "city": "Los Angeles"},
        {"name": "ramy", "age": 17, "city": "Chicago"}
    ]
    
    name = input("Enter a name: ")
    age = input("Enter an age : ")
    city = input("Enter a city : ")
    
    if not age.isdigit():
        print("Invalid age input.")
        return
    age = int(age)
    
    
    found = False
    for entry in data_list:
        if entry["name"].lower() == name.lower() and entry["age"] == age and entry["city"].lower() == city.lower():
            found = True
            break
    
    if found:
        print("The entered data exists in the list!")
    else:
        print("The entered data does not exist in the list.")

check_data_in_dict()
