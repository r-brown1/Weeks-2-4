def add_hobby(name, hobby, data):
    d = [student for student in data if student["name"] == name]
    try:
        print(d[0])
        if "hobbies" in d[0]: # d returns a filtered list containing one element <class 'dict'> or raises an Index Error
            d[0]["hobbies"].append(hobby)
        else:
            d[0]["hobbies"] = [hobby]
    except IndexError:
        print("Student not found")
    finally:
        if len(d) > 0:
            print(f"Hobby <{hobby}> added successfully")
        else:
            print("Failed to add hobby")
