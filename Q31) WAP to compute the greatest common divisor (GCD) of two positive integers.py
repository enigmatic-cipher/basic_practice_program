x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

def gcd(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y

    return y

print(gcd(x, y))

