# Dictionaries - used to store key value pairs of any data
# Each value correspond to one value !
# Nested dictionary - dictionary inside a dictionary, collection of dictionaries in one dictionary

student = {
    "name": "Eveline",
    "id": 145769,
    "feedback": None
}
print(f"{student}\n")

all_students = [
    {"name": "Eveline", "id": 145769, "feedback": None},
    {"name": "Mark", "id": 145779, "feedback": "Excellent student"},
    {"name": "Jason", "id": 145789, "feedback": 5000}
]

for index in all_students:
    print(f"{index}")
print("\n")

# Dictionary data

print("Student first name is {0}".format(student["name"]))
print("Student last name is {0}\n".format(student.get("las name", "unknown"))) # .get method

keys = student.keys()
for element in keys:
    print("The key is: {0}".format(element))
print("\n")

values = student.values()
for value in values:
    print("The value is: {0}".format(value))
print("\n")

student["name"] = "Eva"
del student["feedback"]
print(f"{student}")
