def histogram(lst):
    for i in lst:
        print(i * "$")

lst = []
lent = int(input("Enter the length of list: "))
print("Enter Number",lent)
for i in range(lent):
    data = int(input())
    lst.append(data)

print("Here yours' HISTOGRAM")
histogram(lst)

