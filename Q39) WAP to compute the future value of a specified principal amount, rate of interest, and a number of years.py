"""
FV = PV(1 +r) ^ n

FV	= 	future value
PV	= 	present value
r	= 	annual interest rate
{n}	= 	number of periods interest held
"""

amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))


