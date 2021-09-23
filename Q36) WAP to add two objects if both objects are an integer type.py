def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b

print(add_numbers(6, 5))
print(add_numbers(6, 1.1))

