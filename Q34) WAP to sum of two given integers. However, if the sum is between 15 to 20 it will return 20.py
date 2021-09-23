x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

"""
z = x + y

if (15<=z<=20):
    print("20")

else:
    print(z)
"""

def sum(x, y):
    sum = x + y
    if sum in range(15,20):
        return "Sum is 20"

    else:
        return sum

print(sum(x, y))


