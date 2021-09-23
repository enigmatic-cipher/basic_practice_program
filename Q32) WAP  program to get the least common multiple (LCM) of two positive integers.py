print("LCM Calculator")

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

def lcm(x, y ):
    if x > y:
        z = x

    else:
        z = y

    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break

        z += 1

    return lcm


print(lcm(x, y))
