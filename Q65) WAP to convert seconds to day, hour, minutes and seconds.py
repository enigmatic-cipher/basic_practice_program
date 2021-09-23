import datetime


def convert(n):
    return str(datetime.timedelta(seconds=n))


n = float(input("Enter Seconds to convert: "))
print(convert(n))
