"""
val = input("Enter the interger value: ")
val2 = ['1', '5', '8', '9']

if val in val2:
    print("Value Exist")

else:
    print("Not Exist")
"""
# ---------------------------------------------
"""
def val(data, n):
    for value in data:
        if n == value:
            return True

    return False

print(val([1,2,3,4,5,6,7,8,9], 4))
"""
# ----------------------------------------------
def values(data, n):
    return n in data
print(values([1,2,3,4,5,6,7], 4))