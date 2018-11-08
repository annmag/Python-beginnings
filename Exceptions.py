# Exception handling - try and except blocks of code

student = {
    "name": "Harvey",
    "id": 151009,
    "feedback": None
}

try:
    student_last_name = student["last_name"]  # There's no "last_name" key -> KeyError
except KeyError:
    print("Error finding last_name\n")
except Exception:  # Handling all possible exceptions (but it's too broad)
    print("Unknown error\n")

try:
    name_id = student["name"] + student["id"]  # You can't add an integer to a string -> TypeError
except TypeError as error:  # That enables to print an error description
    print("You cannot add this two together")
    print(error)

print("\nThis code has been executed")
