# def new_strng(str):
#     if len(str) >= 2 and str[:2] == "is":
#         return str
#     else:
#         return "is" + str
#
# print(new_strng(input("Enter new statement: ")))

string = input('insert string -> ')
print('Is' + string if not string.startswith('Is') else string)