number = 1
string = "New string"  # Python is a dynamically typed language
boolean = True

print("hello".capitalize())
print("hello".replace("l", "m"))
print("hello".isalpha())
print("123".isdigit())

splitter = "some,csv,values".split(",")
for name in splitter:
    print(f"{name}")
