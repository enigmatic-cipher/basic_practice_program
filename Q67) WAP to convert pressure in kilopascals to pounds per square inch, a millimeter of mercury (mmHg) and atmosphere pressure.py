pressure = float(input("Enter pressure in kilopascal to convert : "))

pounds_per_sq_inch = pressure * 0.145038
mm_mercury = pressure / 0.133322
atm_pressure =  pressure / 101

print(f"Pressure in  kilopascals to pounds per square inch,a millimeter of mercury (mmHg) and atmosphere pressure is "
      f"{pounds_per_sq_inch}, {mm_mercury}, {atm_pressure}")
