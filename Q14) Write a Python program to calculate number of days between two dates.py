# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date
# objects.
import datetime
from datetime import date
d1 = date(2021, 8, 3)
d2 = date(2021, 8, 9)
no_of_days = d2 - d1
print(no_of_days)

"""
x = datetime.datetime.now()
print(x)
"""