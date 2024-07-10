# Exceptions

print("Calculating the area of a rectangle.")
try:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    if length == 0 or breadth == 0:
        exit("The value can't be 0!")

    area = length * breadth  
    print("Area of a rectangle is", area)

except ValueError as err:
    print("Enter a number")
    print(err)