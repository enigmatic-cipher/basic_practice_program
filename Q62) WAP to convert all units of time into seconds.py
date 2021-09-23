time = float(input("Enter time to convert it into second: "))

value = (input("Enter the time unit: ")).lower()

if value == "hr":
    print(f"time in seconds are: {time * 3600} secs")

if value == "min":
    print(f"Time in seconds are: {time * 60} secs")
