print("Body Mass Index Calculator")

height = int(input("Enter your height in Meter: "))
weight = int(input("Enter your weight in kg: "))

bmi = (weight / height ** 2)

print(f"Your BMI is {bmi}")

