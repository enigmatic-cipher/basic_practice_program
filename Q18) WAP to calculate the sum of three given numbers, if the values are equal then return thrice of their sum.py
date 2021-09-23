def sum_of_num():
    x = int(input("Enter First Number : "))
    y = int(input("Enter Second Number : "))
    z = int(input("Enter Third Number : "))

    if x == y == z:
        print((x + y + z) * 3)

    else:
        print(x + y + z)


print(sum_of_num())
