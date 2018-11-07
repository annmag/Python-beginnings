# If statements
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number isn't 5")

# Concept of truthy and falsy values
if number:
    print("Number is defined and truthy")  # This will be printed

new_number = None
if new_number:
    print("Number is defined and truthy")
else:
    print("Number isn't defined so it's falsy")  # In this statement this will be printed

# Use if statement similarly as above with boolean and none (none has a falsy value)
python_course = True
java_course = False
if python_course:
    print("This will execute")  # This will be printed as mentioned
if java_course:
    print("This won't execute")  # And that won't be printed

# Not if - to check if condition is false
if number != 99:
    print("Number isn't 99")  # This will be printed
if not python_course:
    print("It's not python course")  # This won't be printed

# Multiple if conditions - use keywords "and", "or"
if number == 5 or python_course == False:
    print("This will execute")
if number == 5 and python_course == False:
    print("This won't execute")

# Ternary if statements - mean one-line if statements
a = 1
b = 2
print("a > b") if a > b else print("a <= b")
