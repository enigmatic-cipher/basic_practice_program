print("Area of triangle Calculator")

base = input("Enter Base of Triangle: ")
height = input("Enter height of triangle: ")

def area():
    area = 0.5 * int(base) * int(height)
    return f"\nArea of triangle is {area} in square unit."


print(area())
