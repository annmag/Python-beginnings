# For loop
# In Python it's automatically assumes that you want to start from the first element of the list and increment by 1
# It also detects the length of the list
# Operators "++" and "--" don't exist in Python !

student_list = ["Donna", "Rachel", "Paula", "Katherina", "Ben"]

for name in student_list:
    print(f"Student name: {name}")  # This line will be printed with every element on the list

# Range function - when you want to define numbers like starting point or step, could have 1, 2 or 3 arguments
# range(start, stop, step) - generating numbers from start to stop (not including!) with the diffrence of value step
# range(start, stop), range(stop), Default: step == 1, start == 0

for index in range(10):
    print(f"{index}")
print("\n")

for index in range(5,10):
    print(f"{index}")
print("\n")

for index in range(0,10,2):  # Not including 10 !
    print(f"{index}")
print("\n")

for index in range(0,5,2):  # Printing every other names from the list
    name = student_list[index]
    print(f"{name}")
print("\n")

# Break - to stop executing the loop without reaching the end of the list or range function
for name in student_list:
    if name == "Paula":
        print("Finally found Paula!")
        break
    print(f"Currently testing: {name}")
print("\n")

# Continue - to skip executing the rest of the code, proceed or continue onto the next iteration
for name in student_list:  # It prints all the elements without the one in if condition
    if name == "Katherina":
        continue
    print(f"Currently testing: {name}")