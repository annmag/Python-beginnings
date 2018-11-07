# Basic types in Python: int, string, boolean and none
number = 1
string = "New string"
boolean = True
null = None  # This variable is not associated to any value
# Python is a dynamically typed language

# Some methods using with strings
print("hello".capitalize())  # Result: "Hello"
print("hello".replace("l", "m"))  # Result: "hemmo"
print("hello".isalpha())  # Result: True
print("123".isdigit())  # Result: True

splitter = "some,csv,values".split(",")  # Splitting string into a list using a character given as an argument
for name in splitter:  # Result of splitter: ["some","csv","values"]
    print(f"{name}")  # The for loop writes every element from the list named splitter

# String format function
my_name = "Ana"
machine_name = "HAL"
print("Nice to meet you {0}. I'm {1}.".format(my_name, machine_name))  # Result: "Nice to meet you Ana. I'm HAL."
# Python is 0-based language

# String interpolation
print(f"Nice to meet you {my_name}. I'm {machine_name}.")  # Result as above
