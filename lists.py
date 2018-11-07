# Lists - using to hold multiple objects in one variable
# Having mulitple types in a single is acceptable in Python (but can lead to some bugs)

student_names = ["Mickey", "Ana", "Jessica", "Harvey"]

# Getting list elements
student_1 = student_names[0]  # Result: "Mickey"
student_2 = student_names[1]  # Result: "Ana"
student_3 = student_names[-1]  # Result: "Harvey"
print(f"{student_1}, {student_2}, {student_3}")

# Changing list elements
student_names[2] = "Robert"  # Changes "Jessica" to "Robert" on that list
print(f"{student_names[2]}")

# Some list functions and methods

student_names.append("Louis")  # Adding new element to the end of the list (just one argument!)
del student_names[2]  # Deleting an element from the list - shift to the left
print(f"{student_names}")

check = "Robert" in student_names  # Checking if given element is on the list, result True or False
if check:
    statement = "Robert is on the list."
else:
    statement = "Robert isn't on the list."

number_of_students = len(student_names)  # Returns the number of elements on the list
print(f"Number of students on the list: {number_of_students}. {statement}")

# List slicing - doesn't modify the list, just ignore some elements for example while printing
print(f"{student_names[1:]}")  # Result is the list without the first element (which has index 0)
print(f"{student_names[1:-1]}")  # Result is the list without the first and the last element

