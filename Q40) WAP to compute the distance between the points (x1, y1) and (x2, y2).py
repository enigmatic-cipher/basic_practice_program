import math

x1 = int(input("Enter first X coordinate: "))
y1 = int(input("Enter First Y coordinate: "))

x2 = int(input("Enter second X coordinate: "))
y2 = int(input("Enter second Y coordinate: "))

distance = math.dist([x1, y1], [x2, y2])

print(distance)
