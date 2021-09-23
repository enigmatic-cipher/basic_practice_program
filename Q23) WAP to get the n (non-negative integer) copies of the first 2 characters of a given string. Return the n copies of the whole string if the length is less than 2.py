s = input("Enter the string: ")
n = int(input("Enter the number: "))

s1 = ''
for i in range(n):
    s1 = s1 + s[0:2]

print(s1)