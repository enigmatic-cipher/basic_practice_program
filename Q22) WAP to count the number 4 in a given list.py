"""
list = []

leng = int(input("Enter the length of the list: "))

num = int(input("Enter the number: "))

for i in range(leng):
    data = int(input())
    list.append(data)

print(list)
num2 = int(input("Enter the number you want to count: "))
print(list.count(num2))
"""

def list1(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return  count

print(list1([1,2,3,4,5,6,4,3,4,5,67]))