x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def test(x, y):

    if (x == y) or abs(x - y) == 5 or (x + y) == 5:
        return True

    else:
        return False

print(test(x, y))