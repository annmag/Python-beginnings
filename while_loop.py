# While loop - use to repete some part of code while a condition is true

x = 0
while x <= 10:
    print("Count is: {0}".format(x))
    x += 1
print("\n")

y = 10
while y >= 0:
    print("Count is: {0}".format(y))
    y -= 1
print("\n")

# Infinite while loop - remember to end it with keyword break or in other way (e.g. with changing some values)

z = 10
while z:
    z += 10
    if z == 100:
        print("The end")
        break
    print("The value of z is: {0}".format(z))
