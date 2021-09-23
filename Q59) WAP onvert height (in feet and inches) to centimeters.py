print("Feet & Inch Converter")

value = float(input("Enter the value: "))

con = int(input("Press 1 to convert feet into centimeter or Press 2 to convert inch into centimeter: "))

if con == 1:
    print(f"{value} feet in centimeter is {value * 30.48} cm")

elif con == 2:
    print(f"{value} Inch in centimeter is {value * 2.54} cm")

else:
    print("Invalid Entry")
